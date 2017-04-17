from __future__ import unicode_literals

from django.db import models
from ..user_app.models import User

# Create your models here.
class MessageManager(models.Manager):

	def create_message(self, message, to_user, user):
		message = self.create(message=message, to_user=to_user, user=user)
		return message

	def validate_message(self, data, id):
		errors = []
		if len(data['message'])<8:
			errors.append('Please include at least eight characters in your message.')
			return (False, errors)
		else:
			user = User.objects.get(id=id)
			message = self.create_message(data['message'], int(data['to_user']), user)
			return (True, message)


class Message(models.Model):
	message = models.CharField(max_length=4000)
	to_user = models.CharField(max_length=255)
	user = models.ForeignKey(User)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = MessageManager()


####
class CommentManager(models.Manager):

	def create_comment(self, comment, message, user):
		comment = self.create(comment=comment, message=message, user=user)
		return comment

	def validate_comment(self, data, id):
		errors = []
		if len(data['comment'])<1:
			errors.append('In order to post a comment, please include a non-empty text field')
			return (False, errors)
		else:
			user = User.objects.get(id=id)
			message = Message.objects.get(id=int(data['message']))
			comment = self.create_comment(data['comment'], message, user)
			print comment
			return (True, comment)


class Comment(models.Model):
	comment = models.CharField(max_length=1000)
	user = models.ForeignKey(User)
	message = models.ForeignKey(Message, related_name='comment')
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = CommentManager()

