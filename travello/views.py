from datetime import datetime

from django.shortcuts import render
from .models import EventListing, Place, Reservation
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
    event_listing.clicks += 1
    event_listing.save()
    return render(request, 'displayItem.html', {'event_listing': event_listing})

def check_resrevations(request):
    if not request.user.is_authenticated:
        return render(request, 'reservation.html', {'status': 'not logged in'})
    else:
        eventId = request.POST['event_id']
        event_listing = EventListing.objects.get(id=eventId)
        user = request.user

        if event_listing.available_nr_tickets > 0:
            reservation = Reservation.objects.create(event = event_listing, user = user)
            event_listing.available_nr_tickets -= 1
            event_listing.save()
            return render(request, 'reservation.html', {'status': 'success'})
        else:
            return render(request, 'reservation.html', {'status': 'no tickets available'})

def user_reservations(request):
    user = request.user
    if not user.is_authenticated:
        return render(request, 'user-reservations.html', {'status': 'not logged in'})
    else:
        reservations = Reservation.objects.filter(user=user)
        return render(request, 'user-reservations.html', {'status': 'success', 'reservations': reservations})