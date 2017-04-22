from django.conf.urls import url 
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^users$', views.users, name='users'),
	url(r'^add$', views.add, name='add'),
	url(r'^show(?P<id>\d+)$', views.show, name='show'),
]