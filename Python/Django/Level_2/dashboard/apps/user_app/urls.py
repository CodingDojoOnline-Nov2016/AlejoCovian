from django.conf.urls import url 
from . import views

app_name = 'user_app'

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^loginpage$', views.loginpage, name='loginpage'),
	url(r'^login$', views.login, name='login'),
	url(r'^registration$', views.registration, name='registration'),
	url(r'^register$', views.register, name='register'),
	url(r'^logout$', views.logout, name='logout'),
	###
	url(r'^userinfo/(?P<id>\d+)$', views.userinfo, name='userinfo'),
	url(r'^dashboard$', views.dashboard, name='dashboard'),
	url(r'^edit/(?P<id>\d+)$', views.edit, name='edit'),
]