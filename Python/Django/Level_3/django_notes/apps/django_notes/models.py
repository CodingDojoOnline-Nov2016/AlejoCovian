from __future__ import unicode_literals

from django.db import models

# Create your models here.
class NoteValidation(models.Manager):
	def create_note(self, note):
		note = self.create(note=note)
		return (True, note)

	def validate_and_add(self, data):
		note = self.create_note(data['note'])
		return (True, note)

class Note(models.Model):
	note = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	objects = NoteValidation()