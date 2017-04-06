from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from .models import User
from django.contrib import messages

# Create your views here.
def index(request):
	return render(request, 'selftestloginreg/index.html')

def login(request):
	valid, res = User.objects.login(request.POST)
	if valid:
		request.session['email'] = request.POST['email']
		request.session['statement'] = 'Welcome back to the site.'
		return redirect(reverse('selftestloginreg:success'))
	else:
		for error in res:
			messages.error(request, error)
		return redirect(reverse('selftestloginreg:index'))

def register(request):
	valid, res = User.objects.validate_and_create(request.POST)
	if valid:
		request.session['email'] = request.POST['email']
		request.session['statement'] = 'Thank you for registering! Welcome to the site.'
		return redirect(reverse('selftestloginreg:success'))
	else:
		for error in res:
			messages.error(request, error)
		return redirect(reverse('selftestloginreg:index'))

def success(request):
	context = {
		'users': User.objects.all()
	}
	return render(request, 'selftestloginreg/success.html', context)

def logout(request):
	request.session.clear()
	return redirect(reverse('selftestloginreg:index'))
	