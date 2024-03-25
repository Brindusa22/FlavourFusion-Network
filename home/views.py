from django.shortcuts import render, get_object_or_404, reverse
from django.shortcuts import render
from django.views import generic
from recipes.models import Recipe

# Create your views here.

class HomePageView(generic.ListView):
    model = Recipe
    queryset = Recipe.objects.filter(status=1)
    template_name = "home/home_page.html"


def breakfast_detail(request):
    """
     Displays a list of breakfast recipes.
     Retrieves all the recipes from the database and filters them to render only those with status 1 and meal_type breakfast.
     Ordres the rendered recipes by their creation date, in descending order "
    """

    recipes = Recipe.objects.filter(status=1, meal_type='breakfast').order_by('-created_on')
     
   
    return render(
        request,
        "recipes/index.html",
        {'recipe_list': recipes}
    )