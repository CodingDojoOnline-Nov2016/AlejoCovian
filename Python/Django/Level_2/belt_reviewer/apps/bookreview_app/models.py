from __future__ import unicode_literals

from django.db import models

# Create your models here.
class ReviewManager(models.Manager):
	def validate_and_add(self, data, user_id):
		author = ''
		errors = []
		if errors:
			return (False, errors)


class Review(models.Model):
	review = models.CharField(max_length=1000)
	rating = models.SmallIntegerField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = ReviewManager()

class Book(models.Model):
	title = models.CharField(max_length=255)
	author = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)