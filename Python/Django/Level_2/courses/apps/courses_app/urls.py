from django.conf.urls import url
from . import views

urlpatterns=[
	url(r'^$', views.index),
	url(r'^courses$', views.course),
	url(r'^course/(?P<id>\d+)$', views.show), 
	url(r'^remove/(?P<id>\d+)$', views.remove),
]