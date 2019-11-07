from django import forms
from .models import Recipe, Restriction, Restaurant

class RestrictionForm(forms.ModelForm):
    class Meta:
        model = Restriction
        fields = ('name', 'description', 'image_url',)

class RecipeForm(forms.ModelForm):
    class Meta: 
        model = Recipe
        fields = ('title', 'ingredients', 'instructions', 'restriction',)

class RestaurantForm(forms.ModelForm):
    class Meta: 
        model = Restaurant
        fields = ('name', 'location', 'cuisine', 'restriction', )