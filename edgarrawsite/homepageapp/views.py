from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.utils.html import escape
from django.http import JsonResponse
import datetime, random
from django.contrib.auth.decorators import login_required



import json as json
from .models import TodoList
from loginapp.models import edgar
from loginapp.forms import EdgarForm
from recipes.models import Recipe

from .forms import AuthenticationForm, LoginForm
# Create your views here.
#@login_required(login_url="/home/")
def home(request):
    # grab the max id in the database
    max_id = Recipe.objects.order_by('-id')[0].id
    all_recipes = Recipe.objects.all()
    # grab a random possible id. But, it could not exist if we deleted Something
    random_id1 = random.randint(1, max_id)
    random_object1 = Recipe.objects.filter(id__gte=random_id1)[0]
    random_id2 = random.randint(1, max_id)
    if random_id2 == max_id:
        random_id2 = 1;
    random_object2 = Recipe.objects.filter(id__gte=random_id2).exclude(pk=random_id1)[0]
    random_id3 = random.randint(1, max_id)
    if random_id3 == max_id:
        random_id2 = 1;
    random_object3 = Recipe.objects.filter(id__gte=random_id3).exclude(pk=random_id1).exclude(pk=random_id2)[0]
    random_id4 = random.randint(1, max_id)
    if random_id4 == max_id:
        random_id2 = 1;
    random_object4 = Recipe.objects.filter(id__gte=random_id4).exclude(pk=random_id1).exclude(pk=random_id2).exclude(pk=random_id3)[0]


    todolist = TodoList.objects.all()
    all_recipes = Recipe.objects.all()
    webinfo = edgar.objects.get(pk=1)
    context = {
        'sitename':"EdgarRaw",
        'page_name':"Home - EdgarRaw",
        'all_recipes':all_recipes,
        'random_object1':random_object1,
        'random_object2':random_object2,
        'random_object3':random_object3,
        'random_object4':random_object4,
        'todolist': todolist,
        'webinfo': webinfo,
    }
    return render(request, 'homepageapp/homepage.html', context)

def editwebsite(request):
    webinfo = edgar.objects.get(pk=1)
    if request.method=='POST':
        form = EdgarForm(request.POST, request.FILES, instance=webinfo)
        if form.is_valid():
            webinfo = form.save(commit=False)
            webinfo.save()
            return HttpResponseRedirect("/home/")
    else:
        form = EdgarForm(instance=webinfo)
    context = {
        'webinfo':webinfo,
        'form':form,
    }
    return render(request, 'editwebsite.html', context)
