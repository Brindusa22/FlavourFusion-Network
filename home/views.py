from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.shortcuts import render
from django.views import generic
from recipes.models import Recipe
from .forms import SearchForm

# Create your views here.

def home_page(request):

    search_form = SearchForm()

    return render(
        request,
        "home/home_page.html",
        {"search_form": search_form}
    )


class BreakfastList(generic.ListView):
    """
     Displays a list of breakfast recipes.
     Retrieves all the recipes from the database and filters them to render only those with status 1 and meal_type breakfast.
     Ordres the rendered recipes alphabetically. 
    """

    model = Recipe
    template_name = "recipes/recipes_list.html"
    queryset = Recipe.objects.filter(status=1, meal_type='breakfast').order_by('title')
    paginate_by = 6 
    context_object_name= 'recipes'

    def get_context_data(self, **kwargs):
        """
        Gets the values of the meal_type = 'breakfast' from the database and insert the values into a list, to have it into a human
        readable format.
        Retrieve the first result and assign it to a context variable to pass to the recipe_list template for the <h2> title"
    
        """

        context = super().get_context_data(**kwargs)
        meal_types =list( Recipe.objects.filter(status=1, meal_type='breakfast').values_list('meal_type', flat=True)  )
        context['category'] = (meal_types[0])
  
        
        return context


class MainCourseList(generic.ListView):
    """
    Displays a list of main course recipes.
    Retrieves all the recipes from the database and filters them to render only those with status 1 and meal_type main course.
    Ordres the rendered recipes alphabetically.
    """
    model = Recipe
    template_name = "recipes/recipes_list.html"
    queryset = Recipe.objects.filter(status=1, meal_type='main_course').order_by('title')
    paginate_by = 6 
    context_object_name= 'recipes'


    def get_context_data(self, **kwargs):
        """
        Gets the values of the meal_type = 'main_course' from the database and insert the values into a list, to have it into a human
        readable format.
        Retrieve the first result and assign it to a context variable to pass to the recipe_list template for the <h2> title"
    
        """

        context = super().get_context_data(**kwargs)
        meal_types =list( Recipe.objects.filter(status=1, meal_type='main_course').values_list('meal_type', flat=True)  )
        context['category'] = (meal_types[0])
  

        return context

class SoupList(generic.ListView):
    """
    Displays a list of soup recipes.
    Retrieves all the recipes from the database and filters them to render only those with status 1 and meal_type soup.
    Ordres the rendered recipes alphabetically.
    """
    model = Recipe
    template_name = "recipes/recipes_list.html"
    queryset = Recipe.objects.filter(status=1, meal_type='soup').order_by('title')
    paginate_by = 6
    context_object_name= 'recipes'

    def get_context_data(self, **kwargs):
        """
        Gets the values of the meal_type = 'soup' from the database and insert the values into a list, to have it into a human
        readable format.
        Retrieve the first result and assign it to a context variable to pass to the recipe_list template for the <h2> title"
    
        """

        context = super().get_context_data(**kwargs)
        meal_types =list( Recipe.objects.filter(status=1, meal_type='soup').values_list('meal_type', flat=True)  )
        context['category'] = (meal_types[0])
  
        
        return context 


class AppetizerList(generic.ListView):
    """
    Displays a list of appetizer recipes.
    Retrieves all the recipes from the database and filters them to render only those with status 1 and meal_type appetizer.
    Ordres the rendered recipes alphabetically.
    """
    model = Recipe
    template_name = "recipes/recipes_list.html"
    queryset = Recipe.objects.filter(status=1, meal_type='appetizer').order_by('title')
    paginate_by = 6 
    context_object_name= 'recipes'

    def get_context_data(self, **kwargs):
        """
        Gets the values of the meal_type = 'appetizer' from the database and insert the values into a list, to have it into a human
        readable format.
        Retrieve the first result and assign it to a context variable to pass to the recipe_list template for the <h2> title"
    
        """

        context = super().get_context_data(**kwargs)
        meal_types =list( Recipe.objects.filter(status=1, meal_type='appetizer').values_list('meal_type', flat=True)  )
        context['category'] = (meal_types[0])
  
        
        return context


class SidesList(generic.ListView):
    """
    Displays a list of sides recipes.
    Retrieves all the recipes from the database and filters them to render only those with status 1 and meal_type sides.
    Ordres the rendered recipes alphabetically.
    """
    model = Recipe
    template_name = "recipes/recipes_list.html"
    queryset = Recipe.objects.filter(status=1, meal_type='sides').order_by('title')
    paginate_by = 6 
    context_object_name= 'recipes'

    def get_context_data(self, **kwargs):
        """
        Gets the values of the meal_type = 'sides' from the database and insert the values into a list, to have it into a human
        readable format.
        Retrieve the first result and assign it to a context variable to pass to the recipe_list template for the <h2> title"
    
        """
        context = super().get_context_data(**kwargs)
        meal_types =list( Recipe.objects.filter(status=1, meal_type='sides').values_list('meal_type', flat=True))
        context['category'] = (meal_types[0])
  
        
        return context

class DessertList(generic.ListView):
    """
    Displays a list of dessert recipes.
    Retrieves all the recipes from the database and filters them to render only those with status 1 and meal_type dessert.
    Ordres the rendered recipes alphabetically.
    """
    model = Recipe
    template_name = "recipes/recipes_list.html"
    queryset = Recipe.objects.filter(status=1, meal_type='dessert').order_by('title')
    paginate_by = 6 
    context_object_name= 'recipes'

    def get_context_data(self, **kwargs):
        """
        Gets the values of the meal_type = 'dessert' from the database and insert the values into a list, to have it into a human
        readable format.
        Retrieve the first result and assign it to a context variable to pass to the recipe_list template for the <h2> title"
    
        """

        context = super().get_context_data(**kwargs)
        meal_types =list( Recipe.objects.filter(status=1, meal_type='dessert').values_list('meal_type', flat=True)  )
        context['category'] = (meal_types[0])
  
        
        return context


def search_form(request):
    """
    View to search a recipe in the search field.
    """
    queryset = Recipe.objects.filter(status=1)
    search_form = SearchForm(request.POST)
    posts = []


    if request.method == 'POST':
        if search_form.is_valid():
            search_query = request.POST['query']
            posts = Recipe.objects.filter(title__icontains=search_query)

    search_form =SearchForm()
    
    return render(
        request,
        'home/home_page.html',
        {'search_form' : search_form, 'query' : search_query, 'posts': posts}
        )




   