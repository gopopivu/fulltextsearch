from django.shortcuts import render

from .models import SearchResult
from .forms import SearchResultForm, SearchForm
import urllib
from search_engine.htmlparser import Parser
from search_engine.make_index import MakeIndex
from search_engine.queries import Queries
from django.views.generic.edit import UpdateView
import json

def create_filename(url):
  return '_'.join(url.split('//')[1].split('/'))

def create_html(url):
  html = urllib.urlopen(url).read()
  parser = Parser(html)
  return parser.get_title(), parser.get_text_from_html(), parser.get_normalized_html()

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
  context = {'form': form, 'results': results, 'page_template': 'search/results.html'}
  return render(request, template, context )

def add_index(request, template = 'search/add_index.html', extra_context = None):
  if request.method == 'POST':
    form = SearchResultForm(request.POST)
    if form.is_valid():
      url = request.POST['url']
      title, html, normalized_html = create_html(url)
      first_50_words = ' '.join(html.split()[:20])
      s = SearchResult.objects.create(url=url, html=first_50_words, filename=create_filename(url),
       normalized_html=normalized_html, title=title)
      MakeIndex([s]).save_indexes()
  else:
    form = SearchResultForm()
  return render(request, template, {'form': form})

def get_index(request,template = 'search/get_index.html'):
  index = json.load(open('search_engine/indexes.json'))
  return render(request, template, {'index': index})


def urls(request, template = 'search/urls.html'):
  results = SearchResult.objects.order_by('-id')
  return render(request, template, {'results': results})

class SearchResultUpdate(UpdateView):
    model = SearchResult
    success_url = '/search/urls'
    template_name = 'search/form.html'
    fields = ['title']

    

