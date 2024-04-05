from .models import RecipePostRequest
from django import forms


class RequestForm(forms.ModelForm):
    class Meta:
        model = RecipePostRequest
        fields = ('name',
                  'email',
                  'message')