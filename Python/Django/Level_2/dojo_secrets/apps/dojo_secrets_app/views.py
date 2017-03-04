from django.shortcuts import render, redirect
from .models import User, Message, Like
from django.db.models import Count
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
def index(request):
	if 'user' not in request.session:
		return render(request, 'dojo_secrets_app/index.html')
	else:
		return redirect('/secrets')

def login(request):
	result = User.validation.validatelogin(request.POST['email'], request.POST['password'])
	if result == 2:
		return redirect('/')
	if result == 4:
		return redirect('/')
	else:
		email = request.POST['email']
		getbyemail = User.validation.get(email=email)
		request.session['user'] = {
			'id': getbyemail.id,
			'first_name': getbyemail.first_name,
			'last_name': getbyemail.last_name,
			'email': getbyemail.email
		}
		return redirect('/secrets')

def register(request):
	result = User.validation.validateregister(request.POST['first_name'], request.POST['last_name'], request.POST['email'], request.POST['password'], request.POST['confirm_password'])
	if result == True:
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
		'messages': Message.objects.all().order_by('messagelikes'),
		'likes': Message.messagelikes,
	}
	return render(request, 'dojo_secrets_app/popular.html', context)

def delete(request, id):
	Message.objects.get(id=id).delete()
	return redirect('/secrets')

def like(request):
	print User.validation.all()
	thing = request.POST['user']
	message = Message.objects.get(id=request.POST['message'])
	try:
		Like.objects.get(message=message, user=User.validation.get(id=thing))
	except ObjectDoesNotExist:
		Like.objects.create(message=message, user=User.validation.get(id=thing))
	return redirect('/secrets')

def logout(request):
	del request.session['user']
	return redirect('/')

