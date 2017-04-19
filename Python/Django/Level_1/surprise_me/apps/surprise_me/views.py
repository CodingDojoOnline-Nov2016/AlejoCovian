from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse

# Create your views here.
def index(request):
	return render(request, 'surprise_me/index.html')

def number(request):
	numero = int(request.POST['number'])
	context = {
		'numbers': range(numero+1)
	}
	return render(request, 'surprise_me/results.html', context)

