from django import forms


class SearchForm(forms.Form):
    query = forms.CharField(label='', max_length=300, required=False)