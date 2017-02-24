from django.shortcuts import render, redirect, reverse
from .models import Pet

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
	result = Pet.validation.validate(request.POST['name'], request.POST['description'], request.POST['price'])
	if result == 2:
		return redirect('/new')
	if result == 4:
		return redirect('/new')
	if result == 6:
		return redirect('/new')
	if result == True:
		Pet.validation.create(name=request.POST['name'], description=request.POST['description'], price=request.POST['price'])
		return redirect(reverse('pets:index'))

def destroy(request, id):
	Pet.validation.get(id=id).delete()
	return redirect(reverse('pets:index'))

