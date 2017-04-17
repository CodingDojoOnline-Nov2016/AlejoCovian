from django.shortcuts import render, redirect
from .models import Message, Comment
from django.contrib import messages

# Create your views here.
def index(request):
	return True

def create(request, id):
	valid, res = Message.objects.validate_message(request.POST, id)
	if not valid:
		for error in res:
			messages.error(request, error)
	return redirect(request.META.get('HTTP_REFERER'))

def comment(request, id):
	valid, res = Comment.objects.validate_comment(request.POST, id)
	if not valid:
		for error in res:
			messages.error(request, error)
	return redirect(request.META.get('HTTP_REFERER'))