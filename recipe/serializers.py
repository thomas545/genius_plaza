import re
from rest_framework import serializers
from .models import Recipe, Ingredient, Step


class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ('name',)

    def validate_name(self, value):
        
        if len(value) >= 50 :
            raise serializers.ValidationError("name must be less than 50 letters.")
        return value

class RecipeMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = "__all__"

