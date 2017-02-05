from django.shortcuts import render, HttpResponse
from django.contrib.auth.base_user import BaseUserManager
import random
# Create your views here.
def index(request):
	if 'attempt' not in request.session:
		request.session['attempt'] = 0
	if 'word' not in request.session:
		word = BaseUserManager().make_random_password(length=14, allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
		request.session['word'] = word
	return render(request, 'randomwords/index.html')

def generate(request):
	word = BaseUserManager().make_random_password(length = 14, allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
	request.session['word'] = word
	request.session['attempt'] += 1
	return render(request, 'randomwords/index.html')