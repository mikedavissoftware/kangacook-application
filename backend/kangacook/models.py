from django.db import models

# Create your models here.

class Cuisine(models.Model):
  name = models.CharField(max_length=255)
  famous_dish = models.CharField(max_length=255)
  
class Recipe(models.Model):
  name = models.CharField(max_length=255)
  ingredients = models.CharField(max_length=255)
  cuisine = models.ForeignKey(Cuisine, on_delete=models.CASCADE)