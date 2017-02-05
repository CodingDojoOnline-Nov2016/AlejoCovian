from django.shortcuts import render, redirect, HttpResponse
from .models import People

# Create your views here.
def index(request):
	People.objects.create(first_name="Alex", last_name="Covian")
	people = People.objects.all()
	print (people)
	return render(request, "third_app/index.html")