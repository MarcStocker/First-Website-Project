from django import forms
from .models import Recipe

class RecipeForm(forms.Form):
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

    def save(self, request, commit=True):
        thisrecipe= Recipe()
        thisrecipe.title=self.cleaned_data['title']
        thisrecipe.description=self.cleaned_data['description']
        thisrecipe.ingredients=self.cleaned_data['ingredients']
        thisrecipe.recipe=self.cleaned_data['recipe']
        thisrecipe.image=self.cleaned_data['image']
        if commit:
            thisrecipe.save()
        return thisrecipe

    class Meta:
        model = Recipe
        fields = [ 'title', 'description', 'ingredients', 'recipe', 'image' ]
