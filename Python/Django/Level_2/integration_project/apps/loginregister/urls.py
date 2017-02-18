from django.conf.urls import url 
from . import views

urlpatterns = [
	url(r'^$', views.index),
	url(r'^registration$', views.register, name = 'register'),
	url(r'^login$', views.login, name = 'login'),
	url(r'^logout$', views.logout, name = 'logout'),
	url(r'^success$', views.success, name = 'success'),
]