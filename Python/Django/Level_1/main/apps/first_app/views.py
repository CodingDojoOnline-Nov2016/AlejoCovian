from django.shortcuts import render, HttpResponse, redirect

#CONTROLLER

# Create your views here.
def index(request):
	print ("*" * 100)
	return render(request, "index.html" )

def show(request):
	return render(request, 'show.html') 

def create(request):
	print(request.method)
	if request.method == "POST":
		print request.POST
		print("*"*50)
		print(request.POST)
		print("*"*50)
		return redirect('/')
	else:
		return redirect('/')
	request.session['name'] = request.POST['first_name']
	