from django.shortcuts import render, redirect, reverse
from .models import Pet
from django.contrib import messages

# Create your views here.
def index(request):
	context={
		'pets':Pet.validation.all().order_by('-id')
	}
	return render(request, 'pets_app/index.html', context)

def show(request, id):
	context={
		'id':Pet.validation.get(id=id)
	}
	return render(request, 'pets_app/show.html', context)

def edit(request, id):
	context={
		'id':Pet.validation.get(id=id)
	}
	return render(request, 'pets_app/edit.html', context)

def update(request, id):
	Pet.validation.filter(id=id).update(name=request.POST['name'], description=request.POST['description'], price=request.POST['price'])
	return redirect(reverse('pets:index'))

def new(request):
	return render(request, 'pets_app/add.html')

def create(request):
	valid, res = Pet.validation.validate(request.POST)
	if valid:
		return redirect(reverse('pets:index'))
	else:
		for error in res:
			messages.error(request, error)
		return redirect(reverse('pets:new'))

def destroy(request, id):
	Pet.validation.get(id=id).delete()
	return redirect(reverse('pets:index'))

