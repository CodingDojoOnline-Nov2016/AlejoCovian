from django.shortcuts import render, redirect
from .models import Course

# Create your views here.
def index(request):
	context = {
		'courses': Course.objects.all()
	}
	return render(request, 'courses_app_2ndtry/index.html', context)

def makenew(request):
	Course.objects.create(name=request.POST['name'], description=request.POST['description'])
	thing = Course.objects.all()
	print thing
	return redirect('/')