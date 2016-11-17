from django import forms


class RecipeForm(forms.Form):
    title = forms.CharField(
        label="title",
        max_length=64,
        widget=forms.TextInput()
    )
    description = forms.CharField(
        label="description",
        max_length=500,
        widget=forms.Textarea()
    )
