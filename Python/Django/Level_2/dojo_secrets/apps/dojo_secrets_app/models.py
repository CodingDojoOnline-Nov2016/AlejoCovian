from __future__ import unicode_literals

from django.db import models
from ..dojo_users_app.models import User

# Create your models here.
class MessageValidate():
	def validate(self, message, user):
		if len(message)<=2:
			return False
		else:
			Message.objects.create(message=message, user=user)
			return True

class Message(models.Model):
	message = models.TextField(max_length=1000)
	user = models.ForeignKey(User)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	validation = MessageValidate()

#####

class Like(models.Model):
	user = models.ForeignKey(User)
	message = models.ForeignKey(Message, related_name='messagelikes')
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)


