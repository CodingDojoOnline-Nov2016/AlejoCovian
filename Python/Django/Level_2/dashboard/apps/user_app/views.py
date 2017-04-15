from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib import messages
from .models import User

# Create your views here.
def index(request):
	if 'first_name' in request.session:
		return redirect(reverse('user_app:dashboard'))
	else:
		return render(request, 'user_app/welcome.html')

def loginpage(request):
	return render(request, 'user_app/login.html')

def login(request):
	valid, res = User.objects.login(request.POST)
	if valid:
		user = User.objects.get(email = request.POST['email'])
		request.session['first_name'] = user.first_name
		return redirect(reverse('user_app:dashboard'), request.session['first_name'])
	else:
		for error in res:
			messages.error(request, error)
	return redirect(reverse('user_app:loginpage'))

def registration(request):
	return render(request, 'user_app/register.html')

def register(request):
	errors = []
	valid, res = User.objects.validate_and_add(request.POST)
	if valid:
		return redirect(reverse('user_app:dashboard'))
	else:
		for error in res:
			messages.error(request, error)
		return redirect(reverse('user_app:registration'))

def logout(request):
	request.session.clear()
	return redirect(reverse('user_app:index'))

#####

def dashboard(request):
	context = {
		'users': User.objects.all()
	}
	return render(request, 'user_app/dashboard.html', context)

def userinfo(request):
	return render(request, 'user_app/user.html')



