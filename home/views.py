from django.shortcuts import render, get_object_or_404, reverse
from django.shortcuts import render
from django.views import generic
from recipes.models import Recipe

# Create your views here.

class HomePageView(generic.ListView):
    model = Recipe
    queryset = Recipe.objects.filter(status=1)
    template_name = "home/home_page.html"


class BreakfastList(generic.ListView):
    """
     Displays a list of breakfast recipes.
     Retrieves all the recipes from the database and filters them to render only those with status 1 and meal_type breakfast.
     Ordres the rendered recipes alphabetically. 
    """

    model = Recipe
    template_name = "recipes/index.html"
    queryset = Recipe.objects.filter(status=1, meal_type='breakfast').order_by('title')
    paginate_by = 6 
   

class MainCourseList(generic.ListView):
    """
    Displays a list of main course recipes.
    Retrieves all the recipes from the database and filters them to render only those with status 1 and meal_type main course.
    Ordres the rendered recipes alphabetically.
    """
    model = Recipe
    template_name = "recipes/index.html"
    queryset = Recipe.objects.filter(status=1, meal_type='main_course').order_by('title')
    paginate_by = 6 
   

class SoupList(generic.ListView):
    """
    Displays a list of soup recipes.
    Retrieves all the recipes from the database and filters them to render only those with status 1 and meal_type soup.
    Ordres the rendered recipes alphabetically.
    """
    model = Recipe
    template_name = "recipes/index.html"
    queryset = Recipe.objects.filter(status=1, meal_type='soup').order_by('title')
    paginate_by = 6 


        