from django.shortcuts import render, HttpResponse, redirect
# Create your views here.
def index(request):
	return render(request, 'disappearingninjas/index.html')

def ninjas(request):
	return render(request, 'disappearingninjas/ninjas.html')

def show(request, colour):
	context = {
		"colour": colour
	}
	if colour == 'red':
		return render(request, "disappearingninjas/red.html")
	if colour == 'blue':
		return render(request, "disappearingninjas/blue.html")
	if colour == 'orange':
		return render(request, "disappearingninjas/orange.html")
	if colour == 'purple':
		return render(request, "disappearingninjas/purple.html")
	else:
		return render(request, "disappearingninjas/peach.html")
	return render(request, "disappearingninjas/ninjas.html", context)
