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


@view_function
def process_request(request):
    if request.method == 'POST':
        form = loginForm(request.POST)
        if form.is_valid():
          user = authenticate(username=request.POST['Username'], password=request.POST['Password'])
          login(request, user)
          request.session['pageMessage'] = "Welcome back " + user.username;
          request.session['showMessage'] = True
          return HttpResponseRedirect('/', user)
        else:
            forms.ValidationError("Wrongo")
    else:
        form = loginForm()

    context = {
        'form': form
    }

    return request.dmp.render('index.html', context)
