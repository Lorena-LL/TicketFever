from datetime import datetime

from django.shortcuts import render
from .models import EventListing, Place
from django.http import HttpResponse
# Create your views here.


def index(request):
    eventsList = EventListing.objects.all()
    sortedList = sorted(list(eventsList), key=lambda event: event.clicks, reverse=True)
    sublist = sortedList[:6]
    return render(request, 'index.html', {'eventsList': sublist})

def search(request):
    # Get form data from the request
    city = request.GET.get('city', '').strip()
    date = request.GET.get('date', '').strip()
    category = request.GET.get('category', '').strip()
    budget = request.GET.get('budget', '').strip()

    # Build the filter arguments dynamically based on non-empty fields
    filters = {}
    filterlist = []
    if city:
        filters['place__city__icontains'] = city  # Case-insensitive partial match for city
        filterlist.append(('city', city))
    if date:
        filters['date'] = date  # Exact date match
        filterlist.append(('date', date))
    if category:
        filters['category'] = category
        filterlist.append(('category', category))
    if budget:
        filters['price__lte'] = float(budget)  # Price less than or equal to budget
        filterlist.append(('max budget', budget))

    # Query the database
    eventListings = EventListing.objects.filter(**filters)

    # Return the filtered results
    return render(request, 'search.html', {'eventsList': eventListings, 'filters':filterlist})

def display_item(request):
    eventId = request.POST['event_id']
    event_listing = EventListing.objects.get(id=eventId)
    return render(request, 'displayItem.html', {'event_listing': event_listing})