from django.shortcuts import render, HttpResponse
import datetime

# Create your views here.
def index(request):
	i = datetime.datetime.now()
	DateTime = ("%s/%s/%s" % (i.month,i.day,i.year)) + " " + ("%s:%s:" % (i.hour,i.minute))
	context={
	"DateTime":DateTime
	}
	return render(request, 'timedisplay/page.html', context)