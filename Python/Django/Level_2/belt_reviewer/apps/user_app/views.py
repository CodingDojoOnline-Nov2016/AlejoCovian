from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages

# Create your views here.
def index(request):
	return render(request, 'user_app/index.html')

def login(request):
	valid, res = User.objects.login(request.POST)
	if valid:
		user = User.objects.get(email = request.POST['email'])
		request.session['first_name'] = user.first_name
		return redirect('/success', request.session['first_name'])
	else:
		for error in res:
			messages.error(request, error)
		return redirect('/')

def register(request):
	valid, res = User.objects.validate_register(request.POST)
	if valid:
		request.session['first_name'] = res.first_name
		return redirect('/success')
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