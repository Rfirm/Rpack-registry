from django.conf.urls import patterns, url
from registry import views


urlpatterns = patterns('',
	url(r'^users/$', views.users, name = 'users'),
    url(r'^users/me/$', views.myDetail, name = 'myDetail'),
    url(r'^users/(?P<user_name>\S+)/$', views.detail, name = 'detail'),
    url(r'^signin/$', views.signin, name = 'signin'),
    url(r'^logout/$', views.logout, name = 'logout'),
)

