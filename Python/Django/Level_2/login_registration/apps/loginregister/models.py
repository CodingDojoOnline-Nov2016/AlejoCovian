from __future__ import unicode_literals

from django.db import models

import bcrypt
import re
EMAILregex = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

# Create your models here.
class UserValidate(models.Manager):
	def validate(self, first_name, last_name, email, password, confirm_password):
		if len(first_name) <= 0:
			return 2
		if len(last_name) <= 0:
			return 4
		if len(email) <= 0:
			return 6
		if len(password) <= 8:
			return 8
		if password != confirm_password:
			return 10
		elif not EMAILregex.match(email):
			return 12
		else:
			pw = password.encode()
			hashed = bcrypt.hashpw(pw, bcrypt.gensalt())
			User.validation.create(first_name=first_name, last_name=last_name, email=email, password=hashed)
			print hashed
			return True

	def login(self, email, password):
		user = User.validation.get(email = email)
		pw = password.encode() # encodes password directly from input
		userpassword = user.password.encode()
		if len(email) <= 0:
			return 2
		if len(password) <= 0:
			return 4
		if bcrypt.hashpw(password.encode(), userpassword) == userpassword:
			return True
		else:
			return 6


class User(models.Model):
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	email = models.CharField(max_length=200)
	password = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	validation = UserValidate()
