from django.shortcuts import render, redirect, HttpResponse
import random
from random import randrange

def index(request):
	if 'gold' not in request.session:
		request.session['gold'] = 0
	return render(request, 'ninjagold/index.html')

def process_money(request, methods = ['POST']):
	request.session['gold'] += 1
	request.session['activities'] = 0
	x = round(random.random())
	print x
	if request.POST['building'] == 'farm':
		random_num = randrange(10,20)
		request.session['gold'] += random_num
		request.session['activities'] = random_num

	if request.POST['building'] == 'cave':
		random_num = randrange(5,10)
		request.session['gold'] += random_num
		request.session['activities'] = random_num

	if request.POST['building'] == 'house':
		random_num = randrange(2,5)
		request.session['gold'] += random_num
		request.session['activities'] = random_num

	if request.POST['building'] == 'casino':
		random_num = randrange(-50,50)
		request.session['gold'] -= random_num
		request.session['activities'] = random_num
	return redirect('/')



