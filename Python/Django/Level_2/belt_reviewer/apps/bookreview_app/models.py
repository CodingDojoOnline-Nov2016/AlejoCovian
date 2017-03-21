from __future__ import unicode_literals

from django.db import models

# Create your models here.
class BookManager(models.Manager):
	def pull_recent_books(self):
		books = self.all()
		return books


class Book(models.Model):
	title = models.CharField(max_length=255)
	author = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = BookManager()

class ReviewManager(models.Manager):


class Review(models.Model):
	review = models.TextField(max_length=5500)
	rating = models.SmallIntegerField()
	review_book = models.ForeignKey(Book, related_name = "book_review")
	review_user = models.ForeignKey(User, related_name = "user_review")
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = ReviewManager()
