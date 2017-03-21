from __future__ import unicode_literals

from django.db import models

from ..user_management.models import User

# Create your models here.
class BookManager(models.Manager):
	def pull_recent_books(self):
		books = self.all().order_by("-updated_at")[:5]
		return books

	def create_book(self, title, author):
		book = self.create(title=title, author=author)
		return book

	def show_book_info(self, book_id):
		book_id = int(book_id)
		try: 
			book = self.get(id=book_id)
			print "got the book!"
			response = {
				"author": book.author,
				"title": book.title,
				"book_id": book.id,
				"reviews": Review.objects.filter(review_book=book).order_by('created_at'),
			}
			return (True, response)
		except:
			error = "Something went wrong!"
			return (False, error)

	def update_book(self, data, book_id, user_id):
		book_id = int(book_id)
		user_id = int(user_id)
		review = data['review']
		rating = int(data['rating'])
		errors = []
		if len(review) < 15:
			errors.append("Review must be at least 15 characters long")
		if rating < 0 or rating > 5:
			errors.append("Rating must be between 0 and 5")
		if errors:
			return (False, errors)
		try:
			book = self.get(id=book_id)
			user = User.objects.get(id=user_id)
			review = Review.objects.create_review(review, rating, book, user)
			return (True, review)
		except:
			errors.append("Something went wrong, are you logged in?")
			return (False, errors)


class Book(models.Model):
	title = models.CharField(max_length=255)
	author = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = BookManager()

class ReviewManager(models.Manager):
	 def pull_recent_reviews(self):
	 	reviews=self.all().order_by("-created_at")[:3]
	 	return reviews

	 def create_review(self, review, rating, book, user):
	 	review = self.create(review=review, rating=rating, review_book=book, review_user=user)
	 	return review

	 def validate_and_add(self, data, user_id):
	 	review = data['review']
	 	rating = int(data['rating'])
	 	a_select = data['author-select']
	 	a_text = data['author']
	 	title = data['title']
	 	author = ''
	 	errors = []
	 	if len(review) < 15:
	 		errors.append("Review must be longer than 15 characters")
	 	if rating < 0 or rating > 5:
	 		errors.append("Rating must be between 1 and 5")
	 	if a_text:
	 		author = a_text
	 	elif a_select:
	 		author = a_select
	 	elif not a_text and not a_select:
	 		errors.append("Please select or add an author")
	 	if len(title) < 1:
	 		errors.append("Please enter a title")
	 	if errors:
	 		return (False, errors)
	 	try:
	 		user = User.objects.get(id=user_id)
	 		book = Book.objects.create_book(title, author)
	 		review = self.create_review(review, rating, book, user)
	 		return (True, review)
	 	except:
	 		errors.append("Oops, are you logged in?")
	 		return (False, errors)

	 def destroy_review(self, review_id, user_id):
	 	review_id = int(review_id)
	 	user_id = int(user_id)
	 	try:
	 		review = self.get(id = review_id)
	 		user = User.objects.get(id = user_id)
	 		print review, "*" * 50
	 		if user != review.review_user:
	 			pass
	 			return False
	 		else:
	 			review.delete()
	 			return True
	 	except:
	 		return False

class Review(models.Model):
	review = models.TextField(max_length=5000)
	rating = models.SmallIntegerField()
	review_book = models.ForeignKey(Book, related_name="book_review")
	review_user = models.ForeignKey(User, related_name="user_review")
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = ReviewManager()

	