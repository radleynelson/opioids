from django.conf import settings
from django_mako_plus import view_function, jscontext
from datetime import datetime, timezone
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.shortcuts import render, redirect
from account.forms import loginForm
from account import models as amod
from django.contrib.auth import authenticate, login, logout
from django.core.exceptions import ValidationError

@view_function
def process_request(request):
    context = {

    }
    logout(request)
    return redirect('/account/')


