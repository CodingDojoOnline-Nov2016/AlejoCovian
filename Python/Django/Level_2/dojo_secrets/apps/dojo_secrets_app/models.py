from __future__ import unicode_literals

from django.db import models
import re
import bcrypt
REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# Create your models here.
class UserValidate(models.Manager):
	def validateregister(self, first_name, last_name, email, password, confirm_password):
		if len(first_name)<=2:
			return 2
		if len(last_name)<=2:
			return 4
		if len(email)<=2:
			return 6
		if len(password)<=2:
			return 8
		if password != confirm_password:
			return 10
		elif not REGEX.match(email):
			return 12
		else:
			if User.validation.filter(email=email).exists():
				return 14
			else:
				hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
				User.validation.create(first_name=first_name, last_name=last_name, email=email, password=hashed)
				return True

	def validatelogin(self, email, password):
		if len(email)<=0:
			return 2
		if len(password)<=0:
			return 4
		else:
			try:
				user = User.validation.get(email=email)
				userpassword = user.password.encode()
				if bcrypt.hashpw(password.encode(), userpassword) == userpassword:
					request.session['user'] = user
					return True
				else:
					return 6
			except:
				if not User.validation.filter(email=email).exists() :
					return 8

class User(models.Model):
	first_name = models.CharField(max_length=45)
	last_name = models.CharField(max_length=45)
	email = models.CharField(max_length=255)
	password = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	validation = UserValidate()

#####

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
	likes = models.IntegerField(default=0)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	validation = MessageValidate()

#####

class Like(models.Model):
	user = models.ForeignKey(User)
	message = models.ForeignKey(Message, related_name='messagelikes')
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)




