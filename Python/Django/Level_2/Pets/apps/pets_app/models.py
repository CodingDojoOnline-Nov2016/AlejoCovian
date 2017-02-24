from __future__ import unicode_literals

from django.db import models

# Create your models here.
class PetValidate(models.Manager):
	def validate(self, name, description, price):
		if len(name)<=0:
			return 2
		if len(description)<=0:
			return 4
		if len(price)<=0:
			return 6
		else:
			return True

class Pet(models.Model):
	name = models.CharField(max_length=45)
	description = models.CharField(max_length=200)
	price = models.CharField(max_length=45)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	validation = PetValidate()

