from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.urlresolvers import reverse

# Create your views here.
from .models import Book, Review

def index(req):
	books = Book.objects.pull_recent_books()
	reviews = Review.objects.pull_recent_reviews()
	context = {
		"books": books,
		"reviews": reviews,
	}
	return render(req, "book_review/index.html", context)

def create(req):
	if req.method == "POST":
		valid, res = Review.objects.validate_and_add(req.POST, req.session['user_id'])
		if valid:
			return redirect(reverse('book_review:index'))
		else:
			for error in res:
				messages.error(req, error)
			return redirect(reverse("book_review:new"))
		return redirect(reverse("book_review:new"))

def new(req):
	if 'user_id' not in req.session:
		return redirect(reverse("user_management:index"))
	context = {
		"authors": Book.objects.order_by("author")
	}
	return render(req, "book_review/new.html", context)

def show(req, book_id):
	if req.method == "POST":
		if req.session['user_id']:
			user_id = req.session['user_id']
			valid, res = Book.objects.update_book(req.POST, book_id, user_id)
			if not valid:
				for error in res:
					messages.error(req, error)
		return redirect(reverse('book_review:show', kwargs={'book_id': book_id}))
	else:
		valid, res = Book.objects.show_book_info (book_id)
		if valid:
			print res
			context = {
				"book_info": res,
			}
		else:
			for error in res:
				messages.error(req, error)
			return redirect(reverse('book_review:index'))
	return render(req, 'book_review/book_details.html', context)

def destroy (req, review_id):
	if req.method == 'POST' and req.session['user_id']:
		user_id = req.session['user_id']
		valid = Review.objects.destroy_review(review_id, user_id)
	return redirect(reverse('book_review:index'))

def books(req):
	books = Book.objects.all().order_by('title')
	context = {
		"books": books,
	}
	return render(req, "book_review/books.html", context)
