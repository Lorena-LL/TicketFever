from datetime import datetime

from django.shortcuts import render
from .models import EventListing
from django.http import HttpResponse
# Create your views here.


def index(request):
	eventsList = EventListing.objects.all()
	return render(request, 'index.html', {'eventsList': eventsList})

def search(request):
	eventsList = EventListing.objects.all()
	return render(request, 'search.html', {'eventsList': eventsList})

def displayItem(request):
	return render(request, 'displayItem.html')