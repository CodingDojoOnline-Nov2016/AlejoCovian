from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib import messages
from .models import User

# Create your views here.
def index(request):
	return render(request, 'user_app_user/welcome.html')

def loginpage(request):
	return render(request, 'user_app_user/login.html')

def login(request):
	valid, res = User.objects.login(request.POST)
	if valid:
		user = User.objects.get(email = request.POST['email'])
		request.session['first_name'] = user.first_name
		if int(user.id) == 1:
			return redirect(reverse('message_app:indexadmin'), request.session['first_name'])
		else:
			return redirect(reverse('message_app:index'), request.session['first_name'])
	else:
		for error in res:
			messages.error(request, error)
	return redirect(reverse('user_app:loginpage'))

def registration(request):
	return render(request, 'user_app_user/register.html')

def register(request):
	errors = []
	valid, res = User.objects.validate_and_add(request.POST)
	if valid:
		return redirect(reverse('message_app:index'))
	else:
		for error in res:
			messages.error(request, error)
		return redirect(reverse('user_app:registration'))

def logout(request):
	request.session.clear()
	return redirect(reverse('user_app:index'))

