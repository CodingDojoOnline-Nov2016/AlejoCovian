from __future__ import unicode_literals

from django.db import models
from ..user_app.models import User

# Create your models here. 

class BookManager(models.Manager):

	def create_book(self, title, author):
		book = self.create(title=title, author=author)
		return book

class Book(models.Model):
	title = models.CharField(max_length=255)
	author = models.CharField(max_length=125)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	objects = BookManager()

######

class ReviewManager(models.Manager):

	def create_review(self, review, rating, book, user):
		review = self.create(review=review, rating=rating, book=book, user=user)
		return review

	def validate_and_add(self, data, user_id):
		errors = []
		if len(data['review'])<1:
			errors.append('please write a review')
		if not data['rating']:
			errors.append('please give this book review a rating')
		if not data['add_author']:
			errors.append('please add an author')
		if data['add_book']:
			title = data['add_book']
		elif data['select_book']:
			title = data['select_book']
		if errors:
			return (False, errors)
		else:
			thing1 = data['add_author']
			thing = int(user_id)
			user = User.objects.get(id = thing)
			author = thing1
			book = Book.objects.create_book(title, author)
			review = self.create_review(data['review'], data['rating'], book, user)
			print review
			return (True, review)

class Review(models.Model):
	review = models.CharField(max_length=1000)
	rating = models.SmallIntegerField()
	book = models.ForeignKey(Book)
	user = models.ForeignKey(User)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = ReviewManager()
