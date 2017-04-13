from __future__ import unicode_literals

from django.db import models

# Create your models here.
class UserManager(models.Manager):

	def create_user(self, email, first_name, last_name, user_level):
		user = self.create(email=email, first_name=first_name, last_name=last_name, password=password user_level=user_level)
		return (True, user)

	def hash_password(self, password):
		pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
		return (True, pw_hash)

	def validate_and_add(self, data):
		errors = []
		if len(data['email'])<1:
			errors.append('EMAIL FIELD CANNOT BE LEFT EMPTY.')
		if len(data['first_name'])<1:
			errors.append('FIRST NAME CANNOT BE LEFT BLANK.')
		if len(data['last_name'])<1:
			errors.append('LAST NAME CANNOT BE LEFT BLANK.')
		if len(data['password'])<1:
			errors.append('PASSWORD FIELD CANNOT BE LEFT EMPTY.')
		if errors:
			return (False, errors)
		else:
			password = self.hash_password(data['password'])
			user = self.create_user(data['email'], data['first_name'], data['last_name'], password, data['user_level'])
			return (True, user)


class User(models.Model):
	email = models.CharField(max_length=255)
	first_name = models.CharField(max_length=45)
	last_name = models.CharField(max_length=45)
	password = models.CharField(max_length=255)
	user_level = models.SmallIntegerField()

	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	objects = UserManager()
