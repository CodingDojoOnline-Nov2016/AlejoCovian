from django.conf.urls import url 
from . import views

urlpatterns = [
	url(r'^$', views.index),
	url(r'^login$', views.login),
	url(r'^success$', views.success),
	url(r'^register$', views.register),
	url(r'^logout$', views.logout),
]