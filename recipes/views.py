from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def recipe_list(request):
    return HttpResponse("My Recipes")