from __future__ import unicode_literals

from django.db import models

# Create your models here.
class PetValidate(models.Manager):
	def create_pet(self, name, description, price):
		pet = self.create(name=name, description=description, price=price)
		return True

	def validate(self, data):
		errors = []
		if len(data['name'])<=0:
			errors.append('This pet needs a name')
		if len(data['description'])<=0:
			errors.append('This pet needs a description')
		if len(data['price'])<=0:
			errors.append('This pet needs a price tag')
		if errors:
			return (False, errors)
		else:
			pet = self.create_pet(data['name'], data['description'], data['price'])
			return (True, pet)

	def edit(self, data, id):
		thing = self.filter(id=id)
		if data['name']:
			thing.update(name=data['name'])
		if data['description']:
			thing.update(description=data['description'])
		if data['price']:
			thing.update(price=data['price'])
		return True


class Pet(models.Model):
	name = models.CharField(max_length=45)
	description = models.CharField(max_length=200)
	price = models.CharField(max_length=45)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	validation = PetValidate()

