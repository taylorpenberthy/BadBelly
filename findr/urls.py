from django.urls import path
from . import views


urlpatterns = [
    path('', views.ListRecipe.as_view()),
    path('restrictions/', views.restriction_list, name='restriction_list'),
    path('recipes/', views.recipe_list, name='recipe_list'),
    path('restrictions/<int:pk>', views.restriction_detail,name='restriction_detail'),
    path('recipes/<int:pk>', views.recipe_detail, name='recipe_detail'),
    path('restrictions/<int:pk>/edit', views.restriction_edit, name='restriction_edit'),
    path('recipes/<int:pk>/edit', views.recipe_edit, name='recipe_edit'),
    path('restrictions/new', views.restriction_create, name='restriction_create'),
    path('recipes/new', views.recipe_create, name='recipe_create'),
    path('recipes/<int:pk>/delete', views.recipe_delete, name='recipe_delete'),
    path('restaurants/', views.restaurant_list, name='restaurant_list'),
    path('restaurants/new', views.restaurant_create, name='restaurant_create'),
    path('restaurants/<int:pk>', views.restaurant_detail, name='restaurant_detail'),
   path('restaurants/<int:pk>/delete', views.restaurant_delete, name='restaurant_delete'),
   path('restaurants/<int:pk>/edit', views.restaurant_edit, name='restaurant_edit')
]