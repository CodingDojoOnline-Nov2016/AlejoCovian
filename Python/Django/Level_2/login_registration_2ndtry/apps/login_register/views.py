from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages

# Create your views here.
def index(request):
	if 'user' not in request.session:
		return render(request, 'login_register/index.html')
	else:
		return redirect('/success')

def login(request):
	result = User.validation.login(request.POST['email'], request.POST['password'])
	if result == 2:
		messages.error(request, 'Please input an email to log in')
		return redirect('/')
	if result == 4:
		messages.error(request, 'Please input a password in order to log in')
		return redirect('/')
	if result == 6:
		messages.error(request, 'Password does not match that account')
		return redirect('/')
	if result == 8:
		messages.error(request, 'No matching account')
		return redirect('/')
	if result == True:
		email = request.POST['email']
		user = User.validation.get(email = email)
		request.session['user'] = user.all()
		return redirect('/success')

def register(request):
	result = User.validation.register(request.POST['first_name'], request.POST['last_name'], request.POST['email'], request.POST['password'], request.POST['confirm_password'])
	if result == 2:
		messages.error(request, 'First Name Field must contain a name')
		return redirect('/')
	if result == 4:
		messages.error(request, 'Last Name Field must contain a name')
		return redirect('/')
	if result == 6:
		messages.error(request, 'Email field must not be empty')
		return redirect('/')
	if result == 8:
		messages.error(request, 'Password field must not be empty')
		return redirect('/')
	if result == 10:
		messages.error(request, 'Password confirmation must match password field')
	if result == 12:
		messages.error(request, 'Email must be valid')
	else:
		return redirect('/success')

def success(request):
	users = User.validation.all()
	context = {
		'users': users,
	}
	return render(request, 'login_register/success.html', context)


def logout(request):
	del request.session['user']
	return redirect('/')

