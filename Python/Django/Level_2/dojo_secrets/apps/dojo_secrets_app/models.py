from __future__ import unicode_literals

from django.db import models
from ..dojo_users_app.models import User

# Create your models here.
class MessageValidate():
	def validate(self, message, user_id):
		errors = []
		if len(message)<1:
			errors.append('Please include a message in order to post one ;)')
		if errors:
			return (False, errors)
		else:
			user = User.validation.get(id=user_id)
			message = Message.objects.create(message=message, user=user)
			return (True, message)

	def destroy_secret(self, message_id):
		message_id = int(message_id)
		message = Message.objects.get(id = message_id)
		message.delete()
		return True

class Message(models.Model):
	message = models.TextField(max_length=1000)
	user = models.ForeignKey(User)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	validation = MessageValidate()

#####

class LikeValidate(models.Manager):
	def create_like(self, user, message_id):
		message = Message.objects.get(id = message_id)
		self.create(user=user, message=message)
		print 'yoyoyo'*8

	def validate_like(self, user_id, message_id):
		thing1 = int(message_id)
		message = Message.objects.get(id=thing1)
		thing = int(user_id)
		user = User.validation.get(id=thing)
		try:
			self.get(user=user, message=message)
			print 'hihihi'*8
			return False
		except:
			self.create_like(user, message_id)
			return True

class Like(models.Model):
	user = models.ForeignKey(User)
	message = models.ForeignKey(Message, related_name='messagelikes')
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	validation = LikeValidate()


