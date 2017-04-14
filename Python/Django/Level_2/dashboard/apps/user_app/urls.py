from django.conf.urls import url 
from . import views

app_name = 'user_app'

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^loginpage$', views.loginpage, name='loginpage'),
	url(r'^login$', views.login, name='login'),
	url(r'^registration$', views.registration, name='registration'),
	url(r'^register$', views.register, name='register'),
]