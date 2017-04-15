from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from ..user_app.models import User

# Create your views here.
def index(request):
	context = {
		'users': User.objects.all()
	}
	return render(request, 'message_app_user/dashboard.html', context)
