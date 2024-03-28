from django.contrib import admin
from .models import Recipe, RecipeRating
from django_summernote.admin import SummernoteModelAdmin
import json

@admin.register(Recipe)
class RecipeAdmin(SummernoteModelAdmin):
    
    list_display = ('title', 'author', 'slug', 'created_on', 'status')
    search_fields = ['title', 'ingredients']
    list_filter = ('status', 'created_on')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('description', 'ingredients', 'get_ingredients', 'instructions')
   
# Register your models here.

admin.site.register(RecipeRating)
