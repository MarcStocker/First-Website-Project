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
    print("MaxID: "+str(max_id))
    random_id1 = random.randint(1, max_id)
    print(random_id1)
    random_object1 = Recipe.objects.filter(id__gte=random_id1)[0]
    random_id2 = random.randint(1, max_id)
    print(random_id2)
    random_object2 = Recipe.objects.filter(id__gte=random_id2).exclude(pk=random_id1)[0]
    random_id3 = random.randint(1, max_id)
    print(random_id3)
    random_object3 = Recipe.objects.filter(id__gte=random_id3).exclude(pk=random_id1).exclude(pk=random_id2)[0]
    random_id4 = random.randint(1, max_id)
    print(random_id4)
    random_object4 = Recipe.objects.filter(id__gte=random_id4).exclude(pk=random_id1).exclude(pk=random_id2).exclude(pk=random_id3)[0]
    print(random_id1)
    print(random_id2)
    print(random_id3)
    print(random_id4)
    # return object with that id, or first valid object with id greater than that id


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
