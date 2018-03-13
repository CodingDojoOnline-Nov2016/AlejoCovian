from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from .models import Product
from django.contrib import messages
from django.http import HttpResponse

# Create your views here.
def index(request):
	context = {
		'products':Product.validation.all().order_by('-created_at')
	}
	return render(request, 'product_app/index.html', context)

def show(request, id):
	context = {
		'id':Product.validation.get(id=id)
	}
	return render(request, 'product_app/show.html', context)

def edit(request, id):
	context = {
		'id':Product.validation.get(id=id)
	}
	return render(request, 'product_app/edit.html', context)

def update(request, id):
	Product.validation.update_product(request.POST, id)
	return redirect(reverse('products:index'))

def create_product(request):
	valid, res = Product.validation.validate(request.POST['name'], request.POST['description'],request.POST['price'])
	if valid:
		return redirect(reverse('products:index'))
	else:
		for error in res:
			messages.error(request, error)
		return redirect(reverse('products:index'))

def destroy(request, id):
	Product.validation.get(id=id).delete()
	return redirect(reverse('products:index'))

