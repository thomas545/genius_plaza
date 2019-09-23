from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Recipe(models.Model):
    name = models.CharField(max_length=250)
    user = models.OneToOneField(User, related_name='recipe', on_delete=models.CASCADE)

class Ingredient(models.Model):
    recipe = models.ForeignKey(Recipe, related_name='ingredient', on_delete=models.CASCADE)
    text = models.TextField()

class Step(models.Model):
    recipe = models.ForeignKey(Recipe, related_name='step', on_delete=models.CASCADE)
    step_text = models.TextField()