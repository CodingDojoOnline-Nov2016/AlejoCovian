from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request, 'landscapes/index.html')

def snow(request):
	return render(request, 'landscapes/snow.html')

def desert(request):
	return render(request, 'landscapes/desert.html')
	
def forest(request):
	return render(request, 'landscapes/forest.html')

def vineyard(request):
	return render(request, 'landscapes/vineyard.html')

def tropical(request):
	return render(request, 'landscapes/tropical.html')

