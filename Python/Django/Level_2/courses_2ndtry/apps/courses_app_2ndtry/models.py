from __future__ import unicode_literals

from django.db import models



# Create your models here.
class CourseManager(models.Manager):
	def validate(self, name, description):
		if len(name)<=2:
			return 2
		if len(description)<=4:
			return 4
		else:
			return True

class Course(models.Model):
	name = models.CharField(max_length=55)
	description = models.TextField(max_length=1000)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	validation = CourseManager()
