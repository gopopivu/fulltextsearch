from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'fulltextsearch.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^search/', include('search.urls', namespace = 'search')),
    url(r'^admin/', include(admin.site.urls)),
]
