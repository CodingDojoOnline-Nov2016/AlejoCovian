from __future__ import unicode_literals

from django.db import models
import re, bcrypt

REGEXthing = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# Create your models here.
class UserValidate(models.Manager):
	def register(self, first_name, last_name, email, password, confirm_password):
		if len(first_name)<=0:
			return 2
		if len(last_name)<=0:
			return 4
		if len(email)<=0:
			return 6
		if len(password)<=0:
			return 8
		if password != confirm_password:
			return 10
		elif not REGEXthing.match(email):
			return 12
		else:
			hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
			User.validation.create(first_name=first_name, last_name=last_name, email=email, password=hashed)
			return True

	def login(self, email, password):
		if len(email)<=0:
			return 2
		if len(password)<=0:
			return 4
		else:
			try:
				pw = password.encode()
				user = User.validation.get(email = email)
				userpassword = user.password.encode()
				if bcrypt.hashpw(pw, userpassword) == userpassword:
					return True
				else:
					return 6
			except:
				return 8

class User(models.Model):
	first_name = models.CharField(max_length = 45)
	last_name = models.CharField(max_length = 45)
	email = models.CharField(max_length = 255)
	password = models.CharField(max_length = 255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	validation = UserValidate()

