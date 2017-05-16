from django.shortcuts import render

# Create your views here.
def index(request):
	print 'hello world'
	return render(request, 'hello_world/index.html')