from django.shortcuts import render

from .models import SearchResult
from .forms import SearchResultForm
import urllib
from search_engine.htmlparser import Parser
from search_engine.make_index import MakeIndex

def create_filename(url):
  return '_'.join(url.split('//')[1].split('/'))

def create_html(url):
  html = urllib.urlopen(url).read()
  return Parser(html).get_text_from_html()

def add_index(request, template = 'search/add_index.html', extra_context = None):
  if request.method == 'POST':
    form = SearchResultForm(request.POST)
    if form.is_valid():
      url = request.POST['url']
      s = SearchResult.objects.create(url=url, html=create_html(url), filename=create_filename(url))
      MakeIndex([s]).save_indexes()
  else:
    form = SearchResultForm()
  return render(request, template, {'form': form})
    

