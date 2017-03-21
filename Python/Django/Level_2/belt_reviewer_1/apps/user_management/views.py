from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.urlresolvers import reverse

from .models import User
# Create your views here.
def index(req):
	return render(req, 'user_management/index.html')

def create(req):
	if req.method == "POST":
		valid, res = User.objects.validate_and_register(req.POST)
		if valid:
			req.session['user_id'] = res.id
			req.session['alias'] = res.alias
			return redirect(reverse('book_review:index'))
		else:
			for error in res:
				messages.error(req, error)
	else:
		messages.error(req, "Oops! Something went wrong.")
	return redirect(reverse('user_management:index'))

def show(req, user_id):
	try:
		result = User.objects.get_user_info(user_id)
		context = {
			"user_info": result,
		}
	except:
		messages.error(req, result)
		return render(req, 'user_management/user_details.html')
	return render(req, 'user_management/user_details.html', context)

def login(req):
	if req.method == "POST":
		valid, res = User.objects.login_check(req.POST)
		if valid:
			req.session['user_id'] = res.id
			req.session['alias'] = res.alias
			print req.session['alias']
			return redirect(reverse('book_review:index'))
		else:
			for error in res:
				messages.error(req, error)
	else:
		messages.error(req, "Oops! Something went wrong.")
		return redirect(reverse('user_management:index'))

def logout(req):
	req.session.clear()
	return redirect(reverse('book_review:index'))

	