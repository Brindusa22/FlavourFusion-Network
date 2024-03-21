from django.contrib import admin
from .models import Recipe
from django_summernote.admin import SummernoteModelAdmin
import json

@admin.register(Recipe)
class RecipeAdmin(SummernoteModelAdmin):
    
    list_display = ('title', 'author', 'slug', 'status')
    search_fields = ['title']
    list_filter = ('status',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('description', 'ingredients', 'instructions')

    def get_ingredients(self, instance):
        ingredients_json = instance.ingredients
        ingredients_list = json.loads(ingredients_json.replace("'", '"'))
        formatted_ingredients = "\n ".join([f"{ingredient['name']} : {ingredient['measure']}" for ingredient in ingredients_list])
        return formatted_ingredients
    
    get_ingredients.short_description = 'Ingredients'

    def save_model(self, request, obj, form, change):
        obj.ingredients = self.get_ingredients(obj)
        obj.save()
        super().save_model(request, obj, form, change)

# Register your models here.

