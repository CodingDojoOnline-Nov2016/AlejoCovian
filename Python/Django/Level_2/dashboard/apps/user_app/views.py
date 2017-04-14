from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request, 'user_app_user/welcome.html')

def loginpage(request):
	return render(request, 'user_app_user/login.html')

def registration(request):
	return render(request, 'user_app_user/register.html')