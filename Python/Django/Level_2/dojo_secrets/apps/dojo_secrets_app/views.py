from django.shortcuts import render, redirect
from .models import Message, Like
from django.db.models import Count
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages

# Create your views here.
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

