from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'urls$', views.urls, name='urls'),
    url(r'addindex$', views.add_index, name='add_index'),
    url(r'^$', views.index, name='index'),
]