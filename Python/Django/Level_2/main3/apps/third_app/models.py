from __future__ import unicode_literals

from django.db import models

# Create your models here.
class People(models.Model):
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)