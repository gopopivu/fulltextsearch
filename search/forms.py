from django import forms
from models import SearchResult

class SearchForm(forms.Form):
  search_by_phrase = forms.CharField(label="Sort by phrase", max_length=200)

class SearchResultForm(forms.ModelForm):
  class Meta:
    model = SearchResult
    fields = ['url']