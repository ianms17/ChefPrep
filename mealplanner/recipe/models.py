from django.db import models

# Create your models here.
class FavoriteRecipes(models.Model):
    user_id = models.IntegerField()
    recipe_name = models.CharField(max_length=128)
    recipe_link = models.CharField(max_length=64)
    recipe_id = models.IntegerField()
