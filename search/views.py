from django.shortcuts import render

from .models import SearchResult
from .forms import SearchResultForm, SearchForm
import urllib
from search_engine.htmlparser import Parser
from search_engine.make_index import MakeIndex
from search_engine.queries import Queries
from endless_pagination.decorators import page_template

def create_filename(url):
  return '_'.join(url.split('//')[1].split('/'))

def create_html(url):
  html = urllib.urlopen(url).read()
  parser = Parser(html)
  return parser.get_text_from_html(), parser.get_normalized_html()

def index(request, template = 'search/index.html', extra_context = None):
  if request.method == 'POST':
    form = SearchForm(request.POST)
    phrase = request.POST['search_by_phrase']
    phrase = Parser(phrase).get_normalized_html()
    filenames = Queries(phrase).by_whole_phrase()
    results = SearchResult.objects.filter(filename__in=filenames)
  else:
    form = SearchForm()
    results = []
  context = {'form': form, 'results': results, 'page_template': 'search/result.html'}
  return render(request, template, context )

def add_index(request, template = 'search/add_index.html', extra_context = None):
  if request.method == 'POST':
    form = SearchResultForm(request.POST)
    if form.is_valid():
      url = request.POST['url']
      html, normalized_html = create_html(url)
      first_50_words = ' '.join(html.split()[:50])
      s = SearchResult.objects.create(url=url, html=first_50_words, filename=create_filename(url), normalized_html=normalized_html)
      MakeIndex([s]).save_indexes()
  else:
    form = SearchResultForm()
  return render(request, template, {'form': form})
    

