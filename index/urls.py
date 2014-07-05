from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from index import views


urlpatterns = patterns('',
    url(r'^$', views.index, name="index"),
)

urlpatterns = format_suffix_patterns(urlpatterns)