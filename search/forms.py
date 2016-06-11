from django import forms
from models import SearchResult

class SearchForm(forms.Form):
  search_by_phrase = forms.CharField(label="Search:", max_length=200)

class SearchResultForm(forms.ModelForm):
  class Meta:
    model = SearchResult
    fields = ['url']

class AddDocumentsForm(forms.Form):
	add_documents = forms.URLField(label="Url:", max_length=200)
	max_length = forms.IntegerField(label='Max length', max_value=20, min_value=1)
	max_depth = forms.IntegerField(label='Max Depth', max_value=4, min_value=1)