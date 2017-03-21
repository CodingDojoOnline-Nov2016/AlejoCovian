from django.conf.urls import url
from . import views

app_name = "book_review"

urlpatterns = [
	url(r'^$', views.index, name="index"),
	url(r'^reviews$', views.create, name="create"),
	url(r'^reviews/new$', views.new, name="new"),
	url(r'^books/(?P<book_id>\d+)$', views.show, name="show"),
	url(r'^reviews/(?P<review_id>\d+)$', views.destroy, name="destroy"),
	url(r'^books$', views.books, name='books'),
]