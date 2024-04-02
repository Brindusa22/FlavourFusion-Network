from . import views
from django.urls import path

urlpatterns = [
    path('', views.RecipeList.as_view(), name = 'recipes'),
    path('<slug:slug>/', views.recipe_detail, name= 'recipe_detail'),
    path('cuisine/<str:cuisine>/', views.cuisine_list, name= 'cuisine_list'),
    path('mealtype/<str:meal_type>/', views.meal_type_list, name= 'meal_type_list'),
    path('author/<str:username>/', views.author_list, name= 'author_list'),
]