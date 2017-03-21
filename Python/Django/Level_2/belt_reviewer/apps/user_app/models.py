from __future__ import unicode_literals

from django.db import models

import re
import bcrypt
REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
	def create_user(self, first_name, last_name, email, password):
		user = self.create(first_name=first_name, last_name=last_name, email=email, password=password)
		return user
	def hash_password(self, password):
		password = password.encode()
		hashed_pw = bcrypt.hashpw(password, bcrypt.gensalt())
		return hashed_pw
	def compare_password(self, user, password):
		password = password.encode()
		hashed_pw = user.password.encode()
		if bcrypt.hashpw(password, hashed_pw) == hashed_pw:
			return True
		else:
			return False
	def validate_register(self, data):
		errors = []
		if len(data['first_name'])<1:
			errors.append('Please enter a first name')
		if len(data['last_name'])<1:
			errors.append('Please enter a last name')
		if len(data['email'])<1:
			errors.append('Please enter an email')
		if len(data['password'])<8:
			errors.append('Password must be at least eight characters in length')
		elif not REGEX.match(data['email']):
			errors.append('Please enter a valid password: example@thing.this')
		elif data['password'] != data['confirm_password']:
			errors.append('Password and password confirmation must match')
		if errors:
			return (False, errors)

		try:
			match.get(email=data['email'])
			errors.append('Looks like a user already exists with that email. Please sign in with a different email.')
			return(False, errors)
		except:
			password = self.hash_password(data['password'])
			user = self.create_user(self, data['first_name'], data['last_name'], data['email'], data['password'])
			return(True, user)

	def login(self, data):
		errors = []
		try:
			user = self.get(email=data['email'])
			if self.compare_password(user, data['password']):
				return(True, user)
		except:
			errors.append("Incorrect email or password")
		return (False, errors)

	def get_user_info(self, user_id):
		pass

# Create your models here.
class User(models.Model):
	first_name = models.CharField(max_length=45)
	last_name = models.CharField(max_length=45)
	email = models.CharField(max_length=255)
	password = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	objects = UserManager()