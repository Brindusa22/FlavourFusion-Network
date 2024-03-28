from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Recipe, RecipeRating
from .forms import ReviewForm


# Create your views here.
class RecipeList(generic.ListView):
    queryset = Recipe.objects.filter(status = 1)
    template_name = "recipes/index.html"
    paginate_by = 6

def recipe_detail(request, slug):
    """
    Display an individual recipe.
    An instance of model: recipes.Recipe
    template: 'recipes/recipe_detail.html"
    """

    queryset = Recipe.objects.filter(status=1)
    recipe = get_object_or_404(queryset, slug=slug)
    # Split igredients items in order to itterate through them in the recipe_detail.html template.
    ingredients = recipe.ingredients.split('</p>')

    ratings = RecipeRating.objects.filter(recipe=recipe)
    review = ReviewForm()
    return render(
        request,
        "recipes/recipe_detail.html",
        {"recipe": recipe, 'ingredients': ingredients, 'ratings': ratings, 'review': review},
    )


