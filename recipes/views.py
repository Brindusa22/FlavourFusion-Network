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
    review = recipe.reviews.all().order_by("-created_on")
    # Split igredients items in order to itterate through them in the recipe_detail.html template.
    ingredients = recipe.ingredients.split('</p>')


    if request.method == 'POST':
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
         
            review = review_form.save(commit=False)
            review.recipe = recipe
            review.author = request.user
            review.save()

    else:
        review_form = ReviewForm()
   
    return render(
        request,
        'recipes/recipe_detail.html',
        {'recipe': recipe, 'ingredients': ingredients, 'review_form': review_form, 'review': review}
    )
