from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from pages import views


urlpatterns = patterns('',
    url(r'^$', 'pages.views.index'),
)

urlpatterns = format_suffix_patterns(urlpatterns)