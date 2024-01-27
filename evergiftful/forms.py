from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from .models import *








class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control form-control-lg mb-4'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control form-control-lg mb-4'}))

    class Meta:
        model = User
        fields = ['username', 'password']



class SignUpForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control  form-control-lg mb-4'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control  form-control-lg mb-4'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control  form-control-lg mb-4'}))

    class Meta:
        model = User
        fields = [ 'username', 'password1', 'password2']





class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']

    name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control form-control-lg mb-4', 'placeholder': 'Your Name'})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control form-control-lg mb-4', 'placeholder': 'Your Email'})
    )
    subject = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control form-control-lg mb-4', 'placeholder': 'Subject'})
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control form-control-lg mb-4', 'placeholder': 'Your Message'})
    )






