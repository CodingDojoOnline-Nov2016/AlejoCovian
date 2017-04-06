from __future__ import unicode_literals

from django.db import models
import bcrypt

# Create your models here.
class UserManager(models.Manager):

	def hash_password(self, password):
		hashed_pw = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
		print hashed_pw
		return hashed_pw

	def check_passwords(self, user, password):
		if bcrypt.hashpw(password.encode(), user.password.encode()) == user.password.encode():
			return True
		else:
			return False

	def create_user(self, data):
		hashedpw = self.hash_password(data['password'])
		user = self.create(email = data['email'], password = hashedpw)
		print user.email
		return user

	def validate_and_create(self, data):
		errors = []
		if len(data['email'])<1:
			errors.append('You must include an email in order to register.')
		if len(data['password'])<8:
			errors.append('Password must be at least eight characters.')
		if data['password'] != data['confirm_password']:
			errors.append('Password must match password confirmation.')
		else:
			try:
				self.get(email=data['email'])
				errors.append('Whoops! Looks like this email already exists in the database.')
				return (False, errors)
			except:
				user = self.create_user(data)
				return (True, user)
		if errors:
			return (False, errors)

	def login(self, data):
		errors = []
		if len(data['email'])<1:
			errors.append('You must include an email in order to log in.')
		if len(data['password'])<1:
			errors.append('You must include a password in order to log in.')
		else:
			try:
				user = self.get(email=data['email'])
				if self.check_passwords(user, data['password']):
					return (True, user)
			except:
				errors.append('Incorrect email or password')
		if errors:
			return (False, errors)

class User(models.Model):
	email = models.CharField(max_length=45)
	password = models.CharField(max_length=45)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = UserManager()