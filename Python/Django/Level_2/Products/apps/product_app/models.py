from __future__ import unicode_literals

from django.db import models

# Create your models here.
class ProductValidate(models.Manager):

	def create_product(self, name, description, price):
		product = self.create(name=name, description=description, price=price)
		return product

	def validate(self, name, description, price):
		errors = []
		if len(name)<=1:
			errors.append('product needs a name')
		if len(description)<=1:
			errors.append('product needs a description')
		if len(price)<=1:
			errors.append('product needs a price')
		if len(description)>100:
			errors.append('product description needs to have at least 100 characters')
		if errors:
			return (False, errors)
		else:
			product = self.create_product(name, description, price)
			return (True, product)

	def update(self, data):
		pass

class Product(models.Model):
	name = models.CharField(max_length=45)
	description = models.CharField(max_length=100)
	price = models.CharField(max_length=45)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	validation = ProductValidate()

