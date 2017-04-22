from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Interest(models.Model):
	interest = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)


class UserManager(models.Manager):

	def create_user(self, name):
		user = self.create(name=name)
		user.save()
		return user

	def validate_user(self, data):
		errors = []
		if len(data['name'])<2:
			errors.append('Please input a name with a minimum length of two characters.')
		if len(data['interest'])<5:
			errors.append('Please input an interest with a minimum length of five characters.')
		if len(data['name'])>255:
			errors.append('Name is too long! Please make sure your name is less than 255 characters in length.')
		if len(data['interest'])>255:
			errors.append('Interest field is too long! Please make sure your interest is less than 255 characters long.')
		if errors:
			return (False, errors)
		else:
			try:
				this_user = self.get(name=data['name'])
				try:
					this_interest = Interest.objects.get(interest=data['interest'], user=this_user)
					errors.append('looks like this interest already exists in association with this user.')
					return (False, errors)
				except:
					this_interest = Interest.objects.create(interest=data['interest'])
					this_user.user_interests.add(this_interest)
					this_user.save()
				return (True, interest)

			except:
				try:
					this_interest = Interest.objects.get(interest = data['interest'])
					user = self.create_user(data['name'], this_interest)
					user.user_interests.add(this_interest)
					user.save()
					return (True, user)
				except:
					this_interest = Interest.objects.create(interest = data['interest'])
					user = self.create_user(data['name'])
					user.user_interests.add(this_interest)
					user.save()
					return (True, user)

class User(models.Model):
	name = models.CharField(max_length=255)
	user_interests = models.ManyToManyField(Interest, related_name="users")
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = UserManager()

