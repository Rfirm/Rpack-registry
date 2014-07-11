from django.conf.urls import patterns, url
from registry import views


urlpatterns = patterns('',
	url(r'^users/$', views.users, name = 'users'),
    url(r'^users/(?P<user_name>\S+)/$', views.detail, name = 'detail'),
)

