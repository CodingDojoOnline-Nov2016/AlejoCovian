from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from .models import User, Interest
from django.contrib import messages

# Create your views here.
def index(request):
	return render(request, 'interests_app/index.html')

def add(request):
	valid, res = User.objects.validate_user(request.POST)
	if valid:
		return redirect(reverse('interests:users'))
	else:
		for error in res:
			messages.error(request, error)
		return redirect(reverse('interests:index'))


def users(request):
	context = {
		'users':User.objects.all(),
		'interests': Interest.objects.all()
	}
	return render(request, 'interests_app/users.html', context)

def show(request, id):
	context = {
		'user': User.objects.get(id=id)
	}
	return render(request, 'interests_app/show.html', context)

