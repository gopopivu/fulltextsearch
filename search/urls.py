from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'add_index/$', views.add_index, name='add_index'),
]