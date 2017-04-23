from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Interest(models.Model):
	interest = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return self.interest

####

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
			this_interest = Interest(interest=data['interest'])
			this_interest.save()
			try:
				self.get(name=data['name'])
				user = User.objects.get(name=data['name'])	
			except:
				user = User(name=data['name'])
				user.save()
			user.user_interests.add(this_interest)
			print user.user_interests.all()
			return (True, user)

class User(models.Model):
	name = models.CharField(max_length=255)
	user_interests = models.ManyToManyField(Interest, related_name="interests_of_users")
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = UserManager()

	def __unicode__(self):
		return self.name

