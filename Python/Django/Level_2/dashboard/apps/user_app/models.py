from __future__ import unicode_literals
import bcrypt

from django.db import models

# Create your models here.
class UserManager(models.Manager):

	def create_user(self, email, first_name, last_name, password, description):
		user = self.create(email=email, first_name=first_name, last_name=last_name, password=password, description=description)
		return (True, user)

	def hash_password(self, password):
		pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
		return (True, pw_hash)

	def compare_passwords(self, user, password):
		hashed = user.password.encode()
		if bcrypt.hashpw(password.encode(), hashed) == hashed:
			return True
		else:
			return False

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
		try:
			self.get(email=data['email'])
			errors.append('It appears as though this email already exists in the database.')
			return (False, errors)
		except:
			password = self.hash_password(data['password'])
			user = self.create_user(data['email'], data['first_name'], data['last_name'], password, data['description'])
			return (True, user)

	def login(self, data):
		errors = []
		try:
			user = self.get(email=data['email'])
			self.compare_passwords(user, data['password'])
			return (True, user)
		except:
			errors.append('It appears as though this email does not yet exist in the database.')
			return (False, errors)


class User(models.Model):
	email = models.CharField(max_length=255)
	first_name = models.CharField(max_length=45)
	last_name = models.CharField(max_length=45)
	password = models.CharField(max_length=255)
	description = models.CharField(max_length=4000)

	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	objects = UserManager()
