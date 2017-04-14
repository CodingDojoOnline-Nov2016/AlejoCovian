from django.conf.urls import url 
from . import views 
app_name = 'message_app'

urlpatterns = [
	url(r'^', views.index, name='index')
]