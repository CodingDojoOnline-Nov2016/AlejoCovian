from django.shortcuts import render, redirect
from .models import User, Message, Like
from django.db.models import Count
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages

# Create your views here.
def index(request):
	if 'user' not in request.session:
		return render(request, 'dojo_secrets_app/index.html')
	else:
		return redirect('/secrets')

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
		return redirect('/secrets')
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
		return redirect('/secrets')
	else:
		for error in res:
			messages.error(request, error)
		return redirect('/')

def secrets(request):
	context = {
		'users': User.validation.all(),
		'messages': Message.objects.all().order_by('-id'), 
		'likes': Message.messagelikes,
	}
	return render(request, 'dojo_secrets_app/secrets.html', context)

def newsecret(request):
	user = request.session['user']
	result = Message.validation.validate(request.POST['message'], User.validation.get(id=int(user['id'])))
	if result == True:
		print request.POST['message']
	return redirect('/secrets')

def popular(request):
	context = {
		'users': User.validation.all(),
		'messages': Message.objects.all().order_by('id'),
	}
	return render(request, 'dojo_secrets_app/popular.html', context)

def delete(request, id):
	Message.objects.get(id=id).delete()
	return redirect('/secrets')

def like(request):
	message = Message.objects.get(id=request.POST['message'])
	try:
		Like.objects.get(message=message, user=User.validation.get(id=request.POST['user']))
	except ObjectDoesNotExist:
		Like.objects.create(message=message, user=User.validation.get(id=request.POST['user']))
	return redirect('/secrets')

def likepopular(request):
	message = Message.objects.get(id=request.POST['message'])
	try:
		Like.objects.get(message=message, user=User.validation.get(id=request.POST['user']))
	except ObjectDoesNotExist:
		Like.objects.create(message=message, user=User.validation.get(id=request.POST['user']))
	return redirect('/popular')

def logout(request):
	del request.session['user']
	return redirect('/')

