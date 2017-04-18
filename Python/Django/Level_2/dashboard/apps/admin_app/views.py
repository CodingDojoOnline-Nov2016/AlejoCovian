from django.shortcuts import render, redirect
from ..user_app.models import User
from django.contrib import messages
from django.core.urlresolvers import reverse

# Create your views here.
def index(request):
	return render(request, 'admin_app/new.html')

def create_user(request):
	valid, res = User.objects.validate_and_add(request.POST)
	if not valid:
		for error in res:
			messages.error(request, error)
		return redirect(request.META.get('HTTP_REFERER'))
	else:
		return redirect(reverse('user_app:dashboard'))

def remove(request, id):
	User.objects.get(id=id).delete()
	return redirect(request.META.get('HTTP_REFERER'))