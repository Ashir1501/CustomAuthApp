from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from authapp.models import User, Address
from django.urls import reverse_lazy
from django.views.decorators.cache import cache_control

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url=reverse_lazy("login"))  #reverse_lazy makes sure all the urls are loaded then looks for the provided url
def index(request):
    if request.user.is_authenticated:
        user = User.objects.get(username = request.user.username)
        address = Address.objects.get(user=user)
        return render(request,'blog/index.html',{'user':user,'address':address})
    return redirect(reverse_lazy('login'))