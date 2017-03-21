from django.conf.urls import url 
from . import views 

app_name = "user_management"

urlpatterns = [
	url(r'^$', views.create, name='create'),
	url(r'^new$', views.index, name='index'),
	url(r'^(?P<user_id>\d+)$', views.show, name='show'),
	url(r'^login$', views.login, name='login'),
	url(r'^logout$', views.logout, name='logout'),
]