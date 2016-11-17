from django.shortcuts import render
from django.http import HttpResponse
from django.utils.html import escape
from django.http import JsonResponse
import datetime
from django.contrib.auth.decorators import login_required

import json as json
from .models import TodoList

from .forms import AuthenticationForm, LoginForm
# Create your views here.
#@login_required(login_url="/home/")
def home(request):
    todolist = TodoList.objects.all()
    context = {
        'sitename':"EdgarRaw",
        'page_name':"Home - EdgarRaw",
        'todolist': todolist,
    }
    return render(request, 'homepageapp/homepage.html', context)
