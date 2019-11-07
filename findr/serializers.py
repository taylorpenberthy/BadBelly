from rest_framework import serializers
from .models import Recipe, Restriction

class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('title', 'instructions', 'ingredients', 'restriction',)
        model = Recipe

class RestrictionSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('name', 'description', 'image_url',)
        model = Restriction