from django.shortcuts import render, redirect
from .models import Message, Like
from django.db.models import Count
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages

# Create your views here.
def index(request):
	return render(request, 'dojo_secrets_app/index.html')