from django.conf.urls import patterns, url
from registry import views


urlpatterns = patterns('',
	url(r'^users/$', views.users, name = 'users'),
)

