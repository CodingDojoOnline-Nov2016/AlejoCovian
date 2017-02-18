from django.shortcuts import render, HttpResponse, redirect
import random
from django.core.urlresolvers import reverse

# Create your views here.
def index(request):
	if not 'attempt' in request.session:
		request.session['attempt'] = 0
	return render(request, 'index.html')

def create(request):
	random_word = ""
	letters = ['A', 'Q','E', 'M','I', 'D','O','U']
	for i in range(14):
		letter_index = random.randint(0,len(letters)-1)
		random_word += letters[letter_index]
	request.session['attempt'] += 1
	request.session['word'] = random_word
	return redirect(reverse('randomwords:index'))