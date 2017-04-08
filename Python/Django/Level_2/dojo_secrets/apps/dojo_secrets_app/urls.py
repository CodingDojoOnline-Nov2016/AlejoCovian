from django.conf.urls import url 
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^newsecret$', views.newsecret, name='newsecret'),
	url(r'^popular/', views.popular, name='popular'),
	url(r'^delete/(?P<message_id>\d+)/', views.delete, name='delete'),
]