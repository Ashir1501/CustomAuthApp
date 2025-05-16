from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserForm, AddressForm, LoginForm
from django.contrib import messages
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.views.decorators.cache import cache_control

# Create your views here.
# this tell's browser to not store the cache
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def register(request):
    if request.user.is_authenticated:
        return redirect('index')
    if request.method == 'POST':
        user_form = UserForm(request.POST, request.FILES)
        address_form = AddressForm(request.POST)

        if user_form.is_valid() and address_form.is_valid():   #checks for username or email unique. if form is valid converts data to appropriate python data types and stores in cleaned_data dict
            try:
                user = user_form.save(commit=False) #get the instance of user form before saving it
                address = address_form.save(commit=False) # get the instance of address before saving

                designation = user_form.cleaned_data['designation']
                if not designation:
                    raise IntegrityError("Please enter Designation")
                
                password = user_form.cleaned_data["password"].strip()
                conformation_password = user_form.cleaned_data["confirm_password"].strip()
                if password != conformation_password:
                    raise IntegrityError("Password and confirmation password did not match")
                
                try:
                    validate_password(password, user) # passing user to run validation check -> is password similar to username or email
                except ValidationError as e:
                    for error in e.messages:
                        messages.error(request, error+". Kindly re-upload your profile picture if necessary")
                    return render(request, 'authapp/register.html', {'uform': user_form, 'aform': address_form})

                user.set_password(password)

                user.save()
                address.user = user
                address.save()

                group, created = Group.objects.get_or_create(name=designation)
                user.groups.add(group)

                login(request,user)
                messages.success(request, f"signed in as <b>{user.username}</b>")
                return redirect('index')
            except IntegrityError as e:
                messages.error(request, str(e)+". Kindly re-upload your profile picture if necessary")
                return render(request, 'authapp/register.html', {'uform': user_form, 'aform': address_form})
        else:
            messages.error(request," Kindly re-upload your profile picture if necessary")
            return render(request, 'authapp/register.html',{'uform':user_form,'aform':address_form})                
    else:          
        user_form = UserForm()
        address_form = AddressForm()
        return render(request,'authapp/register.html',{'uform':user_form,'aform':address_form})

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def login_view(request):
    if request.user.is_authenticated:
        return redirect('index')
    if request.method == "POST":
        lform = LoginForm(request.POST)

        if lform.is_valid():
            username = lform.cleaned_data["username"].strip()
            password = lform.cleaned_data["password"]
            
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request,user)
                messages.success(request, f"signed in as <b>{user.username}</b>")
                return redirect('index')
            else:
                messages.error(request, "Invalid username and/or password.")
                return render(request, "authapp/login.html",{'form':lform})
        else:
            return render(request, "authapp/login.html",{'form':lform})
    else:
        lform = LoginForm()
        return render(request, "authapp/login.html",{'form':lform})

@login_required(login_url='login')
def logout_view(request):
    logout(request)
    messages.success(request, f"Logged out successfully.")
    return redirect('login')