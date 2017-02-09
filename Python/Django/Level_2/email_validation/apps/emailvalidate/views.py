from django.shortcuts import render, redirect
from .models import Email

# Create your views here.
def index(request):
	return render(request, 'emailvalidate/index.html')

def login(request):
	result = Email.validation.validate(request.POST['email'])
	if result == True:
		return redirect('/success')
	else:
		return redirect('/')


def success(request):
	context = {
		"emails" : Email.validation.all()
	}
	return render(request, 'emailvalidate/success.html', context)

def remove(request, id):
	context = {
		'id': id
	}
	Email.validation.get(id=id).delete()
	return redirect('/success')

def makenew(request):
	return redirect('/')

