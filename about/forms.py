from django import forms
from .models import RecipePostRequest

class RequestForm(forms.ModelForm):
    class Meta:
        model = RecipePostRequest
        fields = ('name',
                  'email',
                  'message')