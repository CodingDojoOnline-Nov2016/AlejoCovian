from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages
from django.core.urlresolvers import reverse

# Create your views here.
def index(request):
	return render(request, 'user_app/index.html')

def login(request):
	valid, res = User.objects.login(request.POST)
	if valid:
		user = User.objects.get(email = request.POST['email'])
		request.session['first_name'] = user.first_name
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
		return redirect(reverse('bookreview_app:index'))
	else:
		for error in res:
			messages.error(request, error)
		return redirect('/')

def success(request):
	context = {
		'users': User.objects.all()
	}
	return render(request, 'user_app/success.html', context)

def logout(request):
	request.session.clear()
	return redirect('/')

