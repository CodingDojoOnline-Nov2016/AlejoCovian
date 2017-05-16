from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib import messages
from .models import Client, Project

# Create your views here.
def index(request):
	context = {
		'clients': Client.objects.all()
	}
	return render(request, 'client_resources_app/index.html', context)

def add_client(request):
	return render(request, 'client_resources_app/addclient.html')

def create_client(request):
	valid, res = Client.objects.validate_and_add(request.POST)
	if valid:
		return redirect(reverse('client_resources:show'))
	else:
		for error in res:
			messages.error(request, error)
		return redirect(reverse('client_resources:add_client'))

def show(request, id):
	context = {
		'client': Client.objects.get(id=id)
	}
	return render(request, 'client_resources_app/client.html', context)

def show_project(request):
	return render(request, 'client_resources_app/project.html')

def add_project(request, id):
	context = {
		'client': Client.objects.get(id=id)
	}
	return render(request, 'client_resources_app/addproject.html', context)

def create_project(request):
	valid, res = Project.objects.validate_and_add(request.POST)
	if valid:
		return redirect(reverse('client_resources:show_project'))
	else:
		for error in res:
			messages.error(request, error)
		return redirect(request.META.get('HTTP_REFERER'))

