from __future__ import unicode_literals

from django.db import models
import bcrypt

# Create your models here.
class UserManager(models.Manager):
	def create_user(self, first_name, last_name, email, password):
		user = self.create(first_name=first_name, last_name=last_name, email=email, password=password)
		return user

	def hash_password(self, password):
		password = password.encode()
		hashed_password = bcrypt.hashpw(password, bcrypt.gensalt())
		return hashed_password

	def compare_passwords(self, password):
		password = password.encode()
		hashed_pw = user.password.encode()
		if bcrypt.hashpw(password, hashed_pw) == hashed_pw:
			return True
		else:
			return False

	def validate_register(self, data):
		errors=[]
		if len(data['first_name'])<1:
			errors.append('Please enter first name')
		if len(data['last_name'])<1:
			errors.append('Please enter last name')
		if len(data['email'])<1:
			errors.append('Please enter email address')
		if len(data['password'])<8:
			errors.append('Password must be at least eight characters')
		if data['password'] != data['confirm_password']:
			errors.append('Password and password confirmation must match')
		if errors:
			return (False, errors)

		try:
			self.get(email=data['email'])
			errors.append('Whoops! Email already exists in the database')
			return(False, errors)
		except:
			pw_hash = self.hash_password(data['password'])
			self.create_user(data['first_name'], data['last_name'], data['email'], pw_hash)

	def login(request, data):
		password = data['password']
		errors = []
		try:
			user = self.get(email=data['email'])
			if self.compare_passwords(user, password):
				return True
			else:
				return (False, errors)
		except:
			errors.append("Whoops! Looks like that email doesn't exist in the database")
		return (False, errors)

class User(models.Model):
	first_name = models.CharField(max_length=45)
	last_name = models.CharField(max_length=45)
	email = models.CharField(max_length=255)
	password = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	objects = UserManager()