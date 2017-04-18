from django.conf.urls import url 
from . import views

urlpatterns = [
	url(r'^$', views.index, name="index"),
	url(r'^testimonials$', views.testimonials, name="testimonials"),
	url(r'^aboutme$', views.aboutme, name="aboutme"),
	url(r'^projects$', views.projects, name="projects"),
]