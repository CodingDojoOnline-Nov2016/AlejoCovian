from django.shortcuts import render, redirect
from .models import Course

# Create your views here.
def index(request):
	context = {
		'courses': Course.objects.all().order_by('-id')
	}
	return render(request, 'courses_app_2ndtry/index.html', context)

def makenew(request):
	Course.objects.create(name=request.POST['name'], description=request.POST['description'])
	thing = Course.objects.all()
	print thing
	return redirect('/')

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
	return redirect('/')

