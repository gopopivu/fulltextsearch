from django import forms
from models import SearchResult

class SearchResultForm(forms.ModelForm):
    class Meta:
        model = SearchResult
        fields = ['url']