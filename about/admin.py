from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import About, RecipePostRequest

# Register your models here.

@admin.register(About)
class AboutAdmin(SummernoteModelAdmin):

    list_display =('name', 'date_updated',)
    read_only = ('created_on')
    summernote_fields = ('content',)

@admin.register(RecipePostRequest)
class RecipePostRequest(admin.ModelAdmin):

    list_display = ('name', 'message', 'read')

  