from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib import messages
from .models import User
from ..message_app.models import Message

# Create your views here.
def index(request):
	if 'first_name' in request.session:
		return redirect(reverse('user_app:dashboard'))
	else:
		return render(request, 'user_app/welcome.html')

def loginpage(request):
	if 'first_name' in request.session:
		return redirect(reverse('user_app:dashboard'))
	return render(request, 'user_app/login.html')

def login(request):
	valid, res = User.objects.login(request.POST)
	if valid:
		user = User.objects.get(email = request.POST['email'])
		request.session['first_name'] = user.first_name
		request.session['id'] = user.id
		return redirect(reverse('user_app:dashboard'))
	else:
		for error in res:
			messages.error(request, error)
	return redirect(reverse('user_app:loginpage'))

def registration(request):
	if 'first_name' in request.session:
		return redirect(reverse('user_app:dashboard'))
	return render(request, 'user_app/register.html')

def register(request):
	errors = []
	valid, res = User.objects.validate_and_add(request.POST)
	if valid:
		user = User.objects.get(email = request.POST['email'])
		request.session['first_name'] = user.first_name
		request.session['id'] = user.id
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
	if 'first_name' not in request.session:
		return redirect(reverse('user_app:index'))
	context = {
		'users': User.objects.all()
	}
	return render(request, 'user_app/dashboard.html', context)

def edit(request, id):
	context = {
		'user': User.objects.get(id=id)
	}
	return render(request, 'user_app/edit.html', context)

def update_information(request, id):
	User.objects.update_information(request.POST, id)
	return redirect(reverse('user_app:userinfo', kwargs={'id':id}))

def update_password(request, id):
	User.objects.update_password(request.POST, id)
	return redirect(reverse('user_app:userinfo', kwargs={'id':id}))

def update_description(request, id):
	User.objects.update_description(request.POST['description'], id)
	return redirect(reverse('user_app:userinfo', kwargs={'id':id}))

def userinfo(request, id):
	user = User.objects.get(id=id)
	context = {
		'user': user,
		'usermessages': Message.objects.filter(to_user=user.id).order_by('-created_at'),
	}
	print Message.objects.all()
	return render(request, 'user_app/user.html', context)


