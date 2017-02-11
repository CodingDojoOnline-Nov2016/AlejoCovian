from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages

# Create your views here.
def index(request):
	if 'user' not in request.session:
		return render(request, 'loginregister/index.html')
	else:
		return redirect('/success')

def register(request):
	result = User.validation.validate(request.POST['first_name'], request.POST['last_name'], request.POST['email'], request.POST['password'], request.POST['confirm_password'])
	if result == True:
		request.session['user'] = {
			'first_name': request.POST['first_name'],
			'last_name' : request.POST['last_name'],
			'email' : request.POST['email'],
		}
		user = request.session['user']
		return redirect('/success', user)
	if result == 2:
		messages.error(request, 'NO FIRST NAME')
		return redirect('/')
	if result == 4:
		messages.error(request, 'NO SECOND NAME')
		return redirect('/')
	if result == 6:
		messages.error(request, 'NO EMAIL')
		return redirect('/')
	if result == 8:
		messages.error(request, 'NO PASSWORD')
		return redirect('/')
	if result == 10:
		messages.error(request, 'PASSWORDS DO NOT MATCH')
		return redirect('/')
	else:
		return redirect('/')

def login(request):
	result = User.validation.login(request.POST['email'], request.POST['password'])
	if result == True:
		email = request.POST['email']
		getbyemail = User.validation.get(email=email)
		request.session['user'] = {
			'email': email,
			'first_name': getbyemail.first_name
		} 
		user = request.session['user']
		print user
		return redirect('/success', user=user)

	if result == 2:
		messages.error(request, 'NO EMAIL INPUT')
		return redirect('/')

	if result == 4:
		messages.error(request, 'NO PASSWORD INPUT')
		return redirect('/')
	else:
		return redirect('/')

def success(request):
	users = User.validation.all()
	context = {
		'users': users
	}
	return render(request, 'loginregister/success.html', context)

def logout(request):
	request.session.pop('user')
	return redirect('/')


