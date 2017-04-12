from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages
from django.core.urlresolvers import reverse
from ..bookreview_app.models import Review

# Create your views here.
def index(request):
	return render(request, 'user_app/index.html')

def login(request):
	valid, res = User.objects.login(request.POST)
	if valid:
		user = User.objects.get(email = request.POST['email'])
		request.session['first_name'] = user.first_name
		request.session['id'] = user.id
		return redirect(reverse('bookreview_app:index'), request.session['first_name'])
	else:
		print 'yip'*8
		for error in res:
			messages.error(request, error)
		return redirect(reverse('user_app:index'))

def register(request):
	valid, res = User.objects.validate_register(request.POST)
	if valid:
		request.session['first_name'] = res.first_name
		request.session['id'] = res.id
		return redirect(reverse('bookreview_app:index'))
	else:
		for error in res:
			messages.error(request, error)
		return redirect('/')

def details(request, id):
	context = {
		'user' : User.objects.get(id=id),
		'reviews': Review.objects.filter(user=User.objects.get(id=id))
	}
	return render(request, 'user_app/user_details.html', context)

def logout(request):
	request.session.clear()
	return redirect('/')

