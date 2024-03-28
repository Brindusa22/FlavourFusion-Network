from django import forms
from .models import RecipeRating

class ReviewForm(forms.ModelForm):
    class Meta:
        model = RecipeRating
        fields = ('comment',)