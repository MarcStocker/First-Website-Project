from django.shortcuts import render
from django.http import HttpResponse
from django.utils.html import escape
from django.http import JsonResponse
import datetime, random
from django.contrib.auth.decorators import login_required



import json as json
from .models import TodoList
from recipes.models import Recipe

from .forms import AuthenticationForm, LoginForm
# Create your views here.
#@login_required(login_url="/home/")
def home(request):
    # grab the max id in the database
    max_id = Recipe.objects.order_by('-id')[0].id
    # grab a random possible id. But, it could not exist if we deleted Something
    random_id1 = random.randint(1, max_id)
    random_id2 = random.randint(1, max_id)
    random_id3 = random.randint(1, max_id)
    random_id4 = random.randint(1, max_id)
    print(random_id1)
    print(random_id2)
    print(random_id3)
    print(random_id4)
    if random_id1 is random_id2:
        random_id1-1
        random_id2+1
    if random_id2 is random_id3:
        random_id2-1
        random_id3+1
    if random_id3 is random_id4:
        random_id3-1
        random_id4+1
    # return object with that id, or first valid object with id greater than that id
    random_object1 = Recipe.objects.filter(id__gte=random_id1)[0]
    random_object2 = Recipe.objects.filter(id__gte=random_id2)[0]
    random_object3 = Recipe.objects.filter(id__gte=random_id3)[0]
    random_object4 = Recipe.objects.filter(id__gte=random_id4)[0]


    todolist = TodoList.objects.all()
    all_recipes = Recipe.objects.all()
    context = {
        'sitename':"EdgarRaw",
        'page_name':"Home - EdgarRaw",
        'all_recipes':all_recipes,
        'random_object1':random_object1,
        'random_object2':random_object2,
        'random_object3':random_object3,
        'random_object4':random_object4,
        'todolist': todolist,
    }
    return render(request, 'homepageapp/homepage.html', context)
