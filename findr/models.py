from django.db import models
from taggit.managers import TaggableManager
# Create your models here.
class Restriction(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image_url = models.TextField()
    def __str__(self):
        return self.name


class Recipe(models.Model):
    title = models.CharField(max_length=100)
    ingredients = models.TextField()
    instructions = models.TextField()
    restriction = models.ForeignKey(Restriction, on_delete=models.CASCADE, related_name='recipe')
    tags = TaggableManager()
    def __str__(self):
        return self.title

class Restaurant(models.Model):
    name=models.CharField(max_length=100)
    location= models.TextField()
    cuisine =  models.CharField(max_length=100)
    restriction = models.ForeignKey(Restriction, on_delete=models.CASCADE, related_name='restaurant')
    def __str__(self):
        return self.name

        
