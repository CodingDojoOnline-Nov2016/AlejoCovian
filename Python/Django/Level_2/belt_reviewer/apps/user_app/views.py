from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages

# Create your views here.
def index(request):
	return render(request, 'user_app/index.html')

def login(request):
	result = User.objects.login(request.POST)
	if result == True:
		user = User.objects.get(email = request.POST['email'])
		request.session['first_name'] = user.first_name
		return redirect('/success', request.session['first_name'])
	else:
		for error in result:
			messages.error(request, error)
		return redirect('/')

def register(request):
	User.objects.validate_register(request.POST)
	user = User.objects.get(email=request.POST['email'])
	request.session['first_name'] = user.first_name
	return redirect('/success', request.session['first_name'])

def success(request):
	context = {
		'users': User.objects.all()
	}
	return render(request, 'user_app/success.html', context)

def logout(request):
	request.session.clear()
	return redirect('/')