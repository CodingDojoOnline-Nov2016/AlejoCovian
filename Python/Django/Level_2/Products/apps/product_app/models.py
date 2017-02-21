from __future__ import unicode_literals

from django.db import models

# Create your models here.
class ProductValidate(models.Manager):
	def validate(self, name, description, price):
		if len(name)<=1:
			return 2
		if len(description)<=1:
			return 4
		if len(price)<=1:
			return 6
		if len(description)>=100:
			return 8
		else:
			return True

class Product(models.Model):
	name = models.CharField(max_length=45)
	description = models.CharField(max_length=100)
	price = models.CharField(max_length=45)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	validation = ProductValidate()

