from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from .models import Review, Book
from django.contrib import messages

# Create your views here.
def index(request):
	context = {
		'reviews' : Review.objects.all().order_by('-updated_at'),
	}
	return render(request, 'bookreview_app/index.html', context)

def new(request):
	print Review.objects.all()
	print Book.objects.all()
	context = {
		'books' : Book.objects.all(),
	}
	return render(request, 'bookreview_app/new.html', context)

def create(request):
	user_id = request.POST['user_id']
	valid, res = Review.objects.validate_and_add(request.POST, user_id)
	if valid:
		return redirect(reverse('bookreview_app:index'))
	else:
		for error in res:
			messages.error(request, error)
		return redirect(reverse('bookreview_app:new'))