"""
Something goes here right?
"""
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.utils.html import escape
from django.http import JsonResponse
import datetime
from django.contrib.auth.decorators import login_required

import json as json
from .forms import RecipeForm
from .models import Recipe

# Create your views here.

def index(request):
    all_recipes = Recipe.objects.all()
    context = {
        'sitename':"EdgarRaw",
        'page_name':"Recipes",
        'all_recipes':all_recipes,
    }
    return render(request, 'recipes.html', context)

@login_required(login_url="/login/")
def submitRecipe(request):
    if request.method=='POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(request)
            return HttpResponseRedirect('/recipes/')
    else:
        form = RecipeForm()
    context = {
        'sitename':"EdgarRaw",
        'page_name':"Add a Recipe - EdgarRaw",
        'form':form,
    }
    return render(request, 'addrecipe.html', context)

def editRecipe(request, recipe_id):
    recipe = Recipe.objects.get(pk=recipe_id)
    if request.method=='POST':
        form = RecipeForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            form.save(request)
            return HttpResponseRedirect('/recipes/')
    else:
        form = RecipeForm()
    context = {
        'sitename':"EdgarRaw",
        'page_name':"Edit Recipe - EdgarRaw",
        'form':form,
    }
    return render(request, 'editrecipe.html', context)

def viewRecipe(request, recipe_id):
    recipe = Recipe.objects.get(pk=recipe_id)
    context = {
        'sitename':"EdgarRaw",
        'page_name':"Recipes",
        'recipe':recipe,
    }
    return render(request, 'recipeDetails.html', context)

def searchRecipes(request):
    if request.method=='POST':
        search_text = request.POST['term']
    else:
        search_text=''

    searchrecipes = Recipe.objects.filter(title__contains=search_text)

    context = {
        'page_name':"Search Recipes",
        'searchrecipes':searchrecipes,
    }
    return render(request, 'searchforrecipes.html', context)
