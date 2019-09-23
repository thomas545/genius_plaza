from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User

from rest_framework import generics, views, exceptions, permissions, status
from rest_framework.response import Response

from .models import Recipe, Ingredient, Step
from .serializers import RecipeSerializer, RecipeMiniSerializer

class CreateRecipeView(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = RecipeSerializer
    queryset = ''

    def create(self, request, *args, **kwargs):
        user = request.user
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class RecipeListView(generics.ListAPIView):
    serializer_class = RecipeMiniSerializer
    queryset = Recipe.objects.all()


class ListUserRecipeView(views.APIView):
    
    def get(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        queryset = Recipe.objects.filter(user=user)
        serializer = RecipeMiniSerializer(queryset, many=True)
        return Response(serializer.data)

class RecipeListUserView(generics.ListAPIView):
    serializer_class = RecipeSerializer
    
    def get_queryset(self):
        user = self.request.user
        queryset = Recipe.objects.filter(user=user)
        return queryset


class RecipeView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = RecipeSerializer
    queryset = Recipe.objects.all()


    def retrieve(self, request, *args, **kwargs):
        user = request.user
        recipe = self.get_object()
        if recipe.user != user:
            raise exceptions.NotAcceptable("this recipe not belong to you.")
        serializer = self.get_serializer(recipe)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        user = request.user
        recipe = self.get_object()
        if recipe.user != user:
            raise exceptions.NotAcceptable("this recipe not belong to you.")
        serializer = self.get_serializer(recipe, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def destroy(self, request, *args, **kwargs):
        user = request.user
        recipe = self.get_object()
        if recipe.user != user:
            raise exceptions.NotAcceptable("this recipe not belong to you.")
        recipe.delete()
        return Response({"success": "your recipe deleted successfully."}, status=status.HTTP_204_NO_CONTENT)