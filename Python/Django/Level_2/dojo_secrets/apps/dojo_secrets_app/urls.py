from django.conf.urls import url 
from . import views 

urlpatterns = [
	url(r'^$', views.index),
	url(r'^register$', views.register),
	url(r'^login$', views.login),
	url(r'^secrets$', views.secrets),
	url(r'^newsecret$', views.newsecret),
	url(r'^delete/(?P<id>\d+)$', views.delete),
	url(r'^like$', views.like),
	url(r'^likepopular$', views.likepopular),
	url(r'^popular$', views.popular),
	url(r'^logout$', views.logout),
]