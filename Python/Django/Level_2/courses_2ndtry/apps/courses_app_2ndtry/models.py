from __future__ import unicode_literals

from django.db import models



# Create your models here.
class CourseManager(models.Manager):

	def create_course(self, name, description):
		course = self.create(name=name, description=description)
		return (True, course)

	def validate_and_add(self, data):
		errors = []
		if len(data['name'])<=2:
			errors.append('name must contain at least two characters')
		if len(data['description'])<=4:
			errors.append('description must contain at least four characters')
		if errors:
			return (False, errors)
		else:
			course = self.create_course(data['name'], data['description'])
			return (True, course)

class Course(models.Model):
	name = models.CharField(max_length=55)
	description = models.TextField(max_length=1000)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = CourseManager()
