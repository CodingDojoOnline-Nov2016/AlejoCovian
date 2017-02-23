from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from .models import Product

# Create your views here.
def index(request):
	context = {
		'products':Product.validation.all()
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
	Product.validation.filter(id=id).update(name=request.POST['name'], description=request.POST['description'], price=request.POST['price'])
	return redirect(reverse('products:index'))

def new(request):
	return render(request, 'product_app/add.html')

def create(request):
	result = Product.validation.validate(request.POST['name'], request.POST['description'],request.POST['price'])
	if result == 2:
		return redirect(reverse('products:new'))
	if result == 4:
		return redirect(reverse('products:new'))
	if result == 6:
		return redirect(reverse('products:new'))
	if result == 8:
		return redirect(reverse('products:new'))
	else:
		Product.validation.create(name=request.POST['name'], description=request.POST['description'], price=request.POST['price'])
		return redirect(reverse('products:index'))

def destroy(request, id):
	Product.validation.get(id=id).delete()
	return redirect(reverse('products:index'))

