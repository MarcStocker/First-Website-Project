from django.shortcuts import render
from django.http import HttpResponse
from django.utils.html import escape
from django.http import JsonResponse
import datetime
from django.contrib.auth.decorators import login_required

import json as json

from .forms import AuthenticationForm, LoginForm
# Create your views here.
@login_required(login_url="/login/")
def index(request):
    #formname=LoginForm.username()
    #formpass=LoginForm.password()
    form = LoginForm()
    context = {
        'sitename':"EdgarRaw",
        'page_name':"Log In",
        'form':form,
    }
    return render(request, 'login.html', context)
