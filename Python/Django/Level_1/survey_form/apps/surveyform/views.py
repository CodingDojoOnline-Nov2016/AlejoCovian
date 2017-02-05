from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
def index(request):
	if 'count' not in request.session:
		request.session['count'] = 0
	return render(request, "surveyform/index.html")

def process(request):
	request.session['count'] += 1
	request.session['name'] = request.POST['name']
	request.session['location'] = request.POST['location']
	request.session['language'] = request.POST['language']
	return redirect('/result')

def result(request):
	return render(request, "surveyform/result.html")

def goback(request):
	return redirect('/')