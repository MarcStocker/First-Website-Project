from django import forms
from .models import Recipe

import os
class RecipeForm(forms.ModelForm):
    title = forms.CharField(
        label="Title",
        max_length=64,
        help_text="What delicious recipe will you be adding today?",
        widget=forms.TextInput()
    )
    description = forms.CharField(
        label="Description",
        max_length=2500,
        help_text="Write a description, or copy/paste your instagram description...",
        required=False,
        widget=forms.Textarea()
    )
    ingredients = forms.CharField(
        label="Ingredients",
        max_length=2000,
        help_text="Fresh Fruit and veggies!",
        required=False,
        widget=forms.Textarea()
    )
    recipe = forms.CharField(
        label="Recipe",
        max_length=5000,
        help_text="Add the Recipe here...",
        required=False,
        widget=forms.Textarea()
    )
    image = forms.ImageField(
        label="Image",
    )

    def update(self, instance, thefile, commit=True):
        thisrecipe = Recipe(pk=instance)
        thisrecipe.title=self.cleaned_data['title']
        thisrecipe.description=self.cleaned_data['description']
        thisrecipe.ingredients=self.cleaned_data['ingredients']
        thisrecipe.recipe=self.cleaned_data['recipe']
        if thisrecipe.image != self.cleaned_data['image']:
            BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
            dafile = str(thefile)
            print("Dafile: " + dafile)
            path = os.path.join(MEDIA_ROOT, dafile.replace('/', '\\'))
            print("Path: " + path)
            # os.remove(path)
        thisrecipe.image=self.cleaned_data['image']
        print("New Image: " + str(self.cleaned_data['image']))
        if commit:
            thisrecipe.save()
        return thisrecipe

    class Meta:
        model = Recipe
        fields = [ 'title', 'description', 'ingredients', 'recipe', 'image' ]
