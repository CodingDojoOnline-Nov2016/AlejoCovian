from django.shortcuts import render, redirect
from .models import Note
from django.contrib import messages
from django.core.urlresolvers import reverse

# Create your views here.
def index(request):
	context = {
		'notes' : Note.objects.all()
	}
	return render(request, 'django_notes/index.html', context)

def create(request):
	valid, res = Note.objects.validate_and_add(request.POST)
	if not valid:
		for error in res:
			messages.error()
	return redirect(reverse('django_notes:index'))