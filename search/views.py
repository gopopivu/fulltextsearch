from django.shortcuts import render

from .models import SearchResult
from .forms import SearchResultForm

def add_index(request, template = 'search/add_index.html', extra_context = None):
  if request.method == 'POST':
    form = SearchResultForm(request.POST)
  else:
    form = SearchResultForm()
  return render(request, template, {'form': form})
    

