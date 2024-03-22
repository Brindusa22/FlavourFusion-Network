from django.shortcuts import render
from django.views import generic
from recipes.models import Recipe

# Create your views here.

class HomePageView(generic.ListView):
    model = Recipe
    queryset = Recipe.objects.all()[:5]
    template_name = "home/home_page.html"
    