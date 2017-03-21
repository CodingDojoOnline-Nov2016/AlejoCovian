from __future__ import unicode_literals

from django.db import models
from django.db.models import Count

import re
import bcrypt
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# Create your models here.
class UserManager(models.Manager):
	def create_user(self, alias, first, last, email, pw_hash):
		user = self.create(
				alias=alias,
				first_name=first,
				last_name=last,
				email=email,
				pw_hash=pw_hash
			)
		return user

	def hash_password(self, password):
		password = password.encode()
		hashed_pw = bcrypt.hashpw(password, bcrypt.gensalt())
		return hashed_pw

	def compare_passwords(self, user, password):
		password = password.encode()
		hashed_pw = user.pw_hash.encode()
		if bcrypt.hashpw(password, hashed_pw) == hashed_pw:
			return True
		else:
			return False

	def validate_and_register(self, data):
		alias = data['alias']
		first = data['first-name']
		last = data['last-name']
		email = data['email']
		password = data['password']
		confirm = data['confirm']
		errors = []

		if len(alias)<1:
			errors.append('Please enter an alias')
		if len(first)<1:
			errors.append('Please enter a first name')
		if len(last)<1:
			errors.append('Please enter a last name')
		if len(email)<1:
			errors.append('Please enter an email address')
		elif not EMAIL_REGEX.match(email):
			errors.append('Please enter a valid email address')
		if len(password)<8:
			errors.append('Password must be at least 8 characters')
		elif password != confirm:
			errors.append("Passwords do not match")
		if errors:
			return (False, errors)

		try:
			match = self.get(email=email)
			errors.append("A user already exists with that email, please login or sign up with a new email.")
			return(False, errors)
		except:
			pw_hash = self.hash_password(password)
			user = self.create_user(alias, first, last, email, pw_hash)
			return (True, user)

	def login_check(self, data):
		email = data['email']
		password = data['password']
		errors = []
		try:
			user = self.get(email=email)
			if self.compare_passwords(user, password):
				return (True, user)
		except:
			errors.append("Incorrect email or password")

		return (False, errors)

	def get_user_info(self, user_id):
		from ..book_review.models import Book
		user_id = int(user_id)
		try:
			user = self.get(id=user_id)
			print "got user"
			user_reviews = User.objects.filter(id=user_id).annotate(num=Count('user_review'))
			print user_reviews[0].num
			books = Book.objects.filter(book_review__book_review=user)
			print books
			response = {
				'alias': user.alias,
				'first_name': user.first_name,
				'last_name': user.last_name,
				'email': user.email,
				'total_reviews': user_reviews[0].num,
				'books': books,
			}
			return (True, response)
		except:
			print 'ERROR ERROR'
			errors = "There was a problem loading this user."
			return(False, errors)


class User(models.Model):
	alias = models.CharField(max_length=255)
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	email = models.CharField(max_length=255)
	pw_hash = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = UserManager()

	