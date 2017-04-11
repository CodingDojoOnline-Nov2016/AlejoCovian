from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse

# Create your views here.
def index(request):
	print 'hihi'*8
	return render(request, 'bookreview_app/index.html')

def new(request):
	return render(request, 'bookreview_app/new.html')