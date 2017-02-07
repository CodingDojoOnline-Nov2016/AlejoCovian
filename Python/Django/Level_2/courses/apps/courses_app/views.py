from django.shortcuts import render, redirect
from .models import Course

# Create your views here.
def index(request):
	context = {
	'courses' : Course.objects.all()
	}
	return render(request, 'courses_app/index.html', context)

def course(request):
	if request.POST['name']>0 and request.POST['description']>0:
		Course.objects.create(name=request.POST['name'], description=request.POST['description'])
	return redirect('/')

def show(request, id):
	context = {
		"id" : id,
		"course": Course.objects.get(id=id)
	}
	return render(request, 'courses_app/delete.html', context)

def remove(request, id):
	context = {
		"id": id
	}
	Course.objects.get(id=id).delete()
	return redirect('/')

