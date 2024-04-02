from . import views
from django.urls import path

urlpatterns = [
    path('', views.RecipeList.as_view(), name = 'recipes'),
    path('<slug:slug>/', views.recipe_detail, name= 'recipe_detail'),
    path('cuisine/<str:cuisine>/', views.cuisine_list, name= 'cuisine_list')
]