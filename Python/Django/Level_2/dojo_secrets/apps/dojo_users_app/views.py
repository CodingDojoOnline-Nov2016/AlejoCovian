from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages
from django.core.urlresolvers import reverse

# Create your views here.
def index(request):
	if 'user' not in request.session:
		return render(request, 'dojo_users_app/index.html')
	else:
		return redirect(reverse('dojo_secrets:index'))

def login(request):
	valid, res = User.validation.validatelogin(request.POST)
	if valid:
		email = request.POST['email']
		getbyemail = User.validation.get(email=email)
		request.session['user'] = {
			'id': getbyemail.id,
			'first_name': getbyemail.first_name,
			'last_name': getbyemail.last_name,
			'email': getbyemail.email
		}
		return redirect(reverse('dojo_secrets:index'))
	else:
		for error in res:
			messages.error(request, error)
		return redirect('/')

def register(request):
	valid, res = User.validation.validateregister(request.POST)
	if valid:
		email = request.POST['email']
		getbyemail = User.validation.get(email=email)
		request.session['user'] = {
			'id': getbyemail.id,
			'first_name': getbyemail.first_name,
			'last_name': getbyemail.last_name,
			'email': getbyemail.email
		}
		return redirect(reverse('dojo_secrets:index'))
	else:
		for error in res:
			messages.error(request, error)
		return redirect('/')
		
def logout(request):
	del request.session['user']
	return redirect(reverse('dojo_users:index'))

#####
