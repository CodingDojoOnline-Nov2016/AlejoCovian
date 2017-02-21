from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^makenew$', views.makenew, name='makenew'),
	url(r'^show/(?P<id>\d+)$', views.show, name = 'show'),
	url(r'^destroy/(?P<id>\d+)$', views.destroy, name='destroy'),
]