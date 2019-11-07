from django.shortcuts import render, redirect
from .models import Restriction, Recipe, Restaurant
from rest_framework import generics
from .forms import RecipeForm, RestrictionForm, RestaurantForm
# Create your views here.
from .serializers import RecipeSerializer
from django.contrib.auth.decorators import login_required

class ListRecipe(generics.ListCreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

def restriction_list(request):
    restrictions = Restriction.objects.all()
    return render(request, 'findr/restriction_list.html', {'restrictions': restrictions})

def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, 'findr/recipe_list.html', {'recipes': recipes})

def restriction_detail(request, pk):
    restriction = Restriction.objects.get(id=pk)
    return render(request, 'findr/restriction_detail.html', {'restriction': restriction})

def recipe_detail(request, pk):
    recipe = Recipe.objects.get(id=pk)
    return render(request, 'findr/recipe_detail.html' ,{'recipe': recipe})

@login_required
def restriction_edit(request, pk):
    restriction = Restriction.objects.get(pk=pk)
    if request.method == 'POST':
        form = RestrictionForm(request.POST, instance=restriction)
        if form.is_valid():
            restriction = form.save()
            return redirect('restriction_list')
    else:
        form = RestrictionForm(instance=restriction)
    return render(request, 'findr/restriction_form.html', {'form': form})

@login_required
def recipe_edit(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    if request.method == 'POST':
        form = RecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            recipe = form.save()
            return redirect('recipe_list')
    else:
        form = RecipeForm(instance=recipe)
    return render(request, 'findr/recipe_form.html', {'form': form})

@login_required
def restriction_create(request):
    if request.method == 'POST':
        form = RestrictionForm(request.POST)
        if form.is_valid():
            restriction = form.save()
            return redirect('restriction_list')
    else:
        form = RestrictionForm()
    return render(request, 'findr/restriction_form.html', {'form': form})

@login_required
def recipe_create(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            recipe = form.save()
            return redirect('recipe_list')
    else:
        form = RecipeForm()
    return render(request, 'findr/recipe_form.html', {'form': form})

@login_required
def recipe_delete(request, pk):
    Recipe.objects.get(id=pk).delete()
    return redirect('recipe_list')


def restaurant_list(request):
    restaurants = Restaurant.objects.all()
    return render(request, 'findr/restaurant_list.html', {'restaurants': restaurants})

def restaurant_create(request):
    if request.method == 'POST':
        form = RestaurantForm(request.POST)
        if form.is_valid():
            restaurant = form.save()
            return redirect('restaurant_list')
    else: 
        form = RestaurantForm()
    return render(request, 'findr/restaurant_form.html', {'form': form})

def restaurant_detail(request, pk):
    restaurant = Restaurant.objects.get(pk=pk)
    return render(request, 'findr/restaurant_detail.html', {'restaurant': restaurant})
    
def restaurant_delete(request, pk):
    Restaurant.objects.get(id=pk).delete()
    return redirect(restaurant_list)

def restaurant_edit(request, pk):
    restaurant = Restaurant.objects.get(pk=pk)
    if request.method == 'POST':
        form = RestaurantForm(request.POST, instance=restaurant)
        if form.is_valid():
            restaurant = form.save()
            return redirect('restaurant_list')
    else:
        form = RestaurantForm(instance=restaurant)
    return render(request, 'findr/restaurant_form.html', {'form': form})