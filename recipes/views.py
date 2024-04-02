from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib.auth.models import User
from .models import Recipe, RecipeRating
from .forms import ReviewForm


# Create your views here.
class RecipeList(generic.ListView):
    queryset = Recipe.objects.filter(status = 1)
    template_name = "recipes/index.html"
    paginate_by = 6


    def get_context_data(self, **kwargs):
        """
        Add extra context variables with customized data queried from the database and
        filtered, to pass to the index.html template.
        """
        
        context = super().get_context_data(**kwargs)

        # query the databese and filter the users who published a recipe, eliminate duplicate results and order them by name;
        # assign to a context variable to be passed to the index template
        context['authors'] = User.objects.filter(recipes__isnull=False).distinct().order_by('username')
        # query the database to retrieve the values of the meal_type field;
        # add to a set to eliminate duplicate and apply the sorted method to sort the results alphabetically.
        meal_types = Recipe.objects.values_list('meal_type', flat=True)
        unique_mealtypes = set(meal_types)
        context['mealtypes'] = sorted(unique_mealtypes)
        # query to retrieve the values of cuisine filed from the Recipe Model
        # add the results to a set to eliminate duplicate and sort alphabetically
        cuisine = Recipe.objects.values_list('cuisine', flat=True)
        unique_cuisine = set(cuisine)
        context['cuisines'] = sorted(unique_cuisine)

        return context


def recipe_detail(request, slug):
    """
    Display an individual recipe.
    An instance of model: recipes.Recipe
    template: 'recipes/recipe_detail.html"
    """

    queryset = Recipe.objects.filter(status=1)
    recipe = get_object_or_404(queryset, slug=slug)
    reviews = recipe.reviews.all().order_by("-created_on")
    reviews_count = recipe.reviews.count()
    
    # Split igredients items in order to itterate through them in the recipe_detail.html template.
    ingredients = recipe.ingredients.split('</p>')


    if request.method == 'POST':
        review_form = ReviewForm(data=request.POST)
        if review_form.is_valid():
         
            review = review_form.save(commit=False)
            review.recipe = recipe
            review.author = request.user
            
            review.save()

    
    review_form = ReviewForm()
   
    return render(
        request,
        'recipes/recipe_detail.html',
        {'recipe': recipe,
         'ingredients': ingredients,
         'review_form': review_form, 
         'reviews': reviews,
         'reviews_count': reviews_count,
        },
    )
