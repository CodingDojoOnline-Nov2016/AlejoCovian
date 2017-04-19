from django.conf.urls import url 
from . import views

urlpatterns = [
	url(r'^$', views.index, name="index"),
	url(r'^0[1-9]|1[0-1]$', views.snow, name="snow"),
	url(r'^0[1-2]|1[0-9]$', views.desert, name="desert"),
	url(r'^1[2-3]|2[0-9]$', views.forest, name="forest"),
	url(r'^2[3-4]|3[0-9]$', views.vineyard, name="vineyard"),
	url(r'^3[4-5]|4[0-9]$', views.tropical, name="tropical"),
]