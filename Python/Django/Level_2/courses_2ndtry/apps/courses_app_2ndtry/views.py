from django.shortcuts import render, redirect
from .models import Course
from django.contrib import messages

# Create your views here.
def index(request):
	context = {
		'courses': Course.validation.all().order_by('-id')
	}
	return render(request, 'courses_app_2ndtry/index.html', context)

def makenew(request):
	result = Course.validation.validate(request.POST['name'], request.POST['description'])
	if result == 2:
		messages.error(request, 'Name must contain more than two characters.')
		return redirect('/')
	if result == 4:
		messages.error(request, 'Description must contain at least three characters.')
		return redirect('/')
	if result == True:
		Course.validation.create(name=request.POST['name'], description=request.POST['description'])
		return redirect('/')

def show(request, id):
	context={
		'id':id,
		'course':Course.validation.get(id=id)
	}
	return render(request, 'courses_app_2ndtry/show.html', context)

def destroy(request, id):
	context={
		'id':id
	}
	Course.validation.get(id=id).delete()
	return redirect('/')

