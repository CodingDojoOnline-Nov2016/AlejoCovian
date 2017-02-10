from __future__ import unicode_literals

from django.db import models

import bcrypt
import re
EMAILregex = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

# Create your models here.
class UserValidate(models.Manager):
	def validate(self, first_name, last_name, email, password, confirm_password):
		if len(first_name) <= 0:
			return False
		if len(last_name) <= 0:
			return False
		if len(email) <= 0:
			return False
		if len(password) <= 0:
			return False
		if password != confirm_password:
			return False
		elif not EMAILregex.match(email):
			return False
		else:
			User.validation.create(first_name=first_name, last_name=last_name, email=email, password=password)
			password = password.encode()
			hashed = bcrypt.hashpw(password, bcrypt.gensalt())
			return True

	def login(self, email, password):
		user = User.validation.get(email=email, password=password)
		return True


class User(models.Model):
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	email = models.CharField(max_length=200)
	password = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	validation = UserValidate()

