from __future__ import unicode_literals

from django.db import models
import re

EMAILregex = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

# Create your models here.
class EmailValidate(models.Manager):
	def validate(self,email):
		if not EMAILregex.match(email):
			return False
		else:
			Email.validation.create(email = email)
			return True
			


class Email(models.Model):
	email = models.CharField(max_length=200)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	validation = EmailValidate()
