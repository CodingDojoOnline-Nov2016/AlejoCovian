from django.shortcuts import render, redirect
from .models import Course
from django.contrib import messages
from django.core.urlresolvers import reverse

# Create your views here.
def index(request):
	context = {
		'courses': Course.objects.all().order_by('-id')
	}
	return render(request, 'courses_app_2ndtry/index.html', context)

def makenew(request):
	valid, res = Course.objects.validate_and_add(request.POST)
	if not valid:
		for error in res:
			messages.error(request, error)
	return redirect(reverse('courses:index'))

def show(request, id):
	context={
		'id':id,
		'course':Course.objects.get(id=id)
	}
	return render(request, 'courses_app_2ndtry/show.html', context)

def destroy(request, id):
	context={
		'id':id
	}
	Course.objects.get(id=id).delete()
	return redirect(reverse('courses:index'))

