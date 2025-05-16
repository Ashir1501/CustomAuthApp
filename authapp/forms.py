from django import forms
from .models import User, Address

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['line_1','city','state','pin_code']
        widgets = {
            'line_1':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter street Address'}),
            'city': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter City Name'}),
            'state': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter State Name'}),
            'pin_code': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Pin Code'}),
        }

class UserForm(forms.ModelForm):
    choice = [("","Select a Designation"),('Patient','Patient'),('Doctor','Doctor')]

    designation = forms.ChoiceField(required=True,choices=choice,widget=forms.Select(attrs={
        'class':'form-control'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Password'}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Conformation Password'}))


    class Meta:
        model = User
        fields = ['first_name','last_name','profile_picture','username','email']
        widgets = {
            'first_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter First Name'}),
            'last_name': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Last Name'}),
            'profile_picture': forms.FileInput(attrs={'class':'form-control'}),
            'username': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Username'}),
            'email': forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter Email'})
        }

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Enter Username'
    }))

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class':'form-control',
        'placeholder':'Enter Password'
    }))