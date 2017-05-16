from django.conf.urls import url 
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^add_client$', views.add_client, name='add_client'),
	url(r'^show(?P<id>\d+)$', views.show, name='show'),
	url(r'^show_project$', views.show_project, name='show_project'),
	url(r'^add_project(?P<id>\d+)$', views.add_project, name='add_project'),
	url(r'^create_project$', views.create_project, name='create_project'),
	url(r'^create_client$', views.create_client, name='create_client'),

]