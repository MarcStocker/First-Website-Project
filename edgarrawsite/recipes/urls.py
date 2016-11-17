from django.conf.urls import url
from . import views

app_name = "recipes"

urlpatterns = [
    #<WebSite.com>/recipes/
    url(r'^$', views.index, name="index"),
    #<WebSite.com>/recipes/
    url(r'^search$', views.searchRecipes, name="searchRecipes"),
    #<WebSite.com>/recipes/<recipe_id>/
    url(r'^(?P<recipe_id>[0-9]+)/$', views.viewRecipe, name="viewRecipe"),
    #<WebSite.com>/recipes/submit/
    url(r'^submit$', views.submitRecipe, name="submitRecipe"),
    #<WebSite.com>/recipes/<recipe_id>/edit
    url(r'^(?P<recipe_id>[0-9]+)/edit$', views.editRecipe, name="editRecipe"),
]
