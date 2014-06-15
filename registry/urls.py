from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from registry import views

urlpatterns = patterns('',
	url(r'^signup/$', views.SignUp.as_view()),
    url(r'^users/(?P<userId>[0-9]+/$)', views.RegistryDetail.as_view()),
)

urlpatterns = format_suffix_patterns(urlpatterns)
