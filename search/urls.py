from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'urls$', views.urls, name='urls'),
    url(r'addindex$', views.add_index, name='add_index'),
    url(r'getindex$', views.get_index, name='get_index'),
    url(r'download$', views.download, name='download'),
    url(r'^results/(?P<pk>[0-9]+)/$', views.SearchResultUpdate.as_view(), name='search_result_update'),
    url(r'^$', views.index, name='index'),
]