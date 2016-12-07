"""
Something goes here right?
"""
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.utils.html import escape
from django.http import JsonResponse
import datetime
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.db.models import Q

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
        return HttpResponseRedirect("/recipes/")
    if search_text == "":
        return HttpResponseRedirect("/recipes/")

    searchallrecipes = Recipe.objects.filter(Q(title__contains=search_text) |
                                          Q(description__contains=search_text) |
                                          Q(recipe__contains=search_text) |
                                          Q(ingredients__contains=search_text))
    searchtitles = Recipe.objects.filter(title__contains=search_text)
    searchdescriptions = Recipe.objects.filter(description__contains=search_text)
    searchrecipes = Recipe.objects.filter(recipe__contains=search_text)
    searchingredients = Recipe.objects.filter(ingredients__contains=search_text)
    context = {
        'page_name':"Search Recipes",
        'searchallrecipes':searchallrecipes,
        'search_text':search_text,
        'searchtitles':searchtitles,
        'searchdescriptions':searchdescriptions,
        'searchrecipes':searchrecipes,
        'searchingredients':searchingredients,
    }
    return render(request, 'searchforrecipes.html', context)


def editRecipe(request, recipe_id):
    post = Recipe.objects.get(pk=recipe_id)
    thefile = post.image
    if request.method == "POST":
        form = RecipeForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.update(instance=recipe_id, thefile=thefile, commit=False)
            post.save()
            context = {
                'recipe':post,
            }
            return render(request, 'recipeDetails.html', context)
    else:
        form = RecipeForm(instance=post)
    context = {
        'post':post,
        'form':form,
    }
    return render(request, 'editrecipe.html', context)

def delete(request, recipe_id):
    recipe = Recipe.objects.get(pk=recipe_id)
    recipe.delete()
    return HttpResponseRedirect("/recipes/")
