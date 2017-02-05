from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index),
	url(r'^users/(?P<id>\d+)$', views.show) 
]