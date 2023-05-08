from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder' : 'Enter your username...',
        'class': 'registerInput'
    }))

    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'placeholder' : 'Enter your Email...',
        'class': 'registerInput'
    }))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder' : 'Enter your password...',
        'class': 'registerInput'
    }))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder' : 'Repeat your password...',
        'class': 'registerInput'
    }))


