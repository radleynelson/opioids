from django.conf import settings
from django_mako_plus import view_function, jscontext
from datetime import datetime, timezone
from django import forms
from account.forms import loginForm
from account import models as amod
from django.contrib.auth import authenticate, login, logout 
from django.core.exceptions import ValidationError 
from django.shortcuts import render, redirect 
from django.http import HttpResponseRedirect
from account.forms import CustomUserCreationForm

@view_function
def process_request(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            request.session['pageMessage'] = "Thanks for signing up!";
            request.session['showMessage'] = True
            return HttpResponseRedirect('/', user)

    else:
        form = CustomUserCreationForm()

    context = {
        'form': form
    }

    return request.dmp.render('sign-up.html', context)

