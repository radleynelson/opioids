from django import forms 
from django.contrib.auth.models import User
import django.contrib.auth
from django.contrib.auth import authenticate, login, logout 
from django.core.exceptions import ValidationError 
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from account import models as amod

class loginForm(forms.Form):
    Username = forms.CharField()
    Password = forms.CharField(max_length=32, widget=forms.PasswordInput)

    def clean(self):
        #data = self.cleaned_data['Password']
        user = authenticate(username=self.cleaned_data['Username'], password=self.cleaned_data['Password'])
        if user is None:
            #ValueError("Username or password is incorrect")
            raise forms.ValidationError('Invalid Username or Password.')
        return self.cleaned_data

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = amod.User
        fields = ('username', 'email')

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = amod.User
        fields = ('username', 'email')