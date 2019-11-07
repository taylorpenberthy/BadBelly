from django.contrib import admin
from .models import Restriction, Recipe, Restaurant
# Register your models here.
admin.site.register(Restriction)
admin.site.register(Recipe)
admin.site.register(Restaurant)