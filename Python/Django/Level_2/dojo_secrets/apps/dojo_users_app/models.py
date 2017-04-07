from __future__ import unicode_literals

from django.db import models
import re
import bcrypt
REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# Create your models here.
class UserValidate(models.Manager):
	def create_user(self, first_name, last_name, email, password):
		self.create(first_name=first_name, last_name=last_name, email=email, password=password)

	def hash_password(self, password):
		hashed_pw = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
		return hashed_pw

	def compare_passwords(self, user, password):
		password = password.encode()
		hashed_pw = user.password.encode()
		if bcrypt.hashpw(password, hashed_pw) == hashed_pw:
			return True
		else:
			return False

	def validateregister(self, data):
		password = data['password']
		errors = []
		if len(data['first_name'])<=1:
			errors.append('First name must not be empty')
		if len(data['last_name'])<=1:
			errors.append('Last name must not be empty')
		if len(data['email'])<=1:
			errors.append('Email cannot be left empty')
		if len(data['password'])<=7:
			errors.append('Password must contain at least eight characters')
		if data['password'] != data['confirm_password']:
			errors.append('Passwords must match')
		if self.filter(email=data['email']).exists():
			errors.append('Whoops! Looks like that email is already in our database')
		if errors:
			return (False, errors)
		else:
			pw_hash = self.hash_password(password)
			user = self.create_user(data['first_name'], data['last_name'], data['email'], pw_hash)
			return (True, user)


	def validatelogin(self, data):
		errors = []
		if len(data['email'])<1:
			errors.append('Please include an email in order to log in')
		if len(data['password'])<1:
			errors.append('Please input your password in order to log in')
		if errors:
			return (False, errors)
		try:
			user = self.get(email=data['email'])
			if self.compare_passwords(user, data['password']):
				return (True, user)
			else:
				errors.append("Password does not match account")
				return(False, errors)
		except:
			errors.append('Whoops! Looks like your account does not yet exist')
			return (False, errors)

class User(models.Model):
	first_name = models.CharField(max_length=45)
	last_name = models.CharField(max_length=45)
	email = models.CharField(max_length=255)
	password = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	validation = UserValidate()

#####



