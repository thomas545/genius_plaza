from django.urls import path
from . import views




urlpatterns = [
    path('create/recipe/', views.CreateRecipeView.as_view()),
    path('recipe-list/', views.RecipeListView.as_view()),
    path('users/recipe-list/', views.RecipeListUserView.as_view()),
    path('recipe-list/user/<int:pk>/', views.ListUserRecipeView.as_view()),
    path('recipe/<int:pk>/', views.RecipeView.as_view()),
]
