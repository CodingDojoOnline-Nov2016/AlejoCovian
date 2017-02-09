from django.conf.urls import url 
from . import views

urlpatterns = [
	url(r'^$', views.index),
	url(r'^login$', views.login),
	url(r'^success$', views.success),
	url(r'^makenew$', views.makenew),
	url(r'^remove/(?P<id>\d+)$', views.remove),
]