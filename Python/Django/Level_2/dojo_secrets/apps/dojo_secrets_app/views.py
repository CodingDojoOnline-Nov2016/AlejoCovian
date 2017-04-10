from django.shortcuts import render, redirect
from .models import Message, Like
from django.db.models import Count
from django.core.urlresolvers import reverse

# Create your views here.
def index(request):
	context = {
		'messages': Message.objects.all().order_by('-created_at')
	}
	return render(request, 'dojo_secrets_app/index.html', context)

def newsecret(request):
	thing = request.session['user']
	user_id = thing['id']
	valid, res = Message.validation.validate(request.POST['message'], user_id)
	return redirect(reverse('dojo_secrets:index'))

def popular(request):
	context = {
		'messages': Message.objects.annotate(thing=Count('messagelikes')).order_by('-thing')
	}
	return render(request, 'dojo_secrets_app/popular.html', context)

def delete(request, message_id):
	valid = Message.validation.destroy_secret(message_id)
	return redirect(reverse('dojo_secrets:index'))

def like(request, message_id):
	thing = request.session['user']
	user_id = thing['id']
	Like.validation.validate_like(user_id, message_id)
	return redirect(request.META.get('HTTP_REFERER'))
