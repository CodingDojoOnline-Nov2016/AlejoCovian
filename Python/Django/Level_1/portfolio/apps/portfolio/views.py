from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request, 'portfolio/index.html')

def testimonials(request):
	return render(request, 'portfolio/testimonials.html')

def aboutme(request):
	return render(request, 'portfolio/aboutme.html')

def projects(request):
	return render(request, 'portfolio/projects.html')