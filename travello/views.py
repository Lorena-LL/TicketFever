from datetime import datetime

from django.shortcuts import render, redirect
from .models import EventListing, Place, Reservation, Message
from django.http import HttpResponse
# Create your views here.


def index(request):
    eventsList = EventListing.objects.all()
    eventsList = eventsList.filter(cancelled=False)
    sortedList = sorted(list(eventsList), key=lambda event: event.clicks, reverse=True)
    sublist = sortedList[:6]

    has_new_messages = False
    if request.user.is_authenticated:
        has_new_messages = Message.objects.filter(user=request.user, is_read=False).exists()

    return render(request, 'index.html', {'eventsList': sublist, 'has_new_messages': has_new_messages,})

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
    eventListings = eventListings.filter(cancelled=False)

    has_new_messages = False
    if request.user.is_authenticated:
        has_new_messages = Message.objects.filter(user=request.user, is_read=False).exists()

    # Return the filtered results
    return render(request, 'search.html', {'eventsList': eventListings, 'filters':filterlist, 'has_new_messages': has_new_messages,})

def display_item(request):
    eventId = request.POST['event_id']
    event_listing = EventListing.objects.get(id=eventId)
    event_listing.clicks += 1
    event_listing.save()

    has_new_messages = False
    if request.user.is_authenticated:
        has_new_messages = Message.objects.filter(user=request.user, is_read=False).exists()

    return render(request, 'displayItem.html', {'event_listing': event_listing, 'has_new_messages': has_new_messages,})

def check_resrevations(request):
    if not request.user.is_authenticated:
        has_new_messages = False
        return render(request, 'reservation.html', {'status': 'not logged in', 'has_new_messages': has_new_messages,})
    else:
        eventId = request.POST['event_id']
        event_listing = EventListing.objects.get(id=eventId)
        user = request.user

        has_new_messages = Message.objects.filter(user=request.user, is_read=False).exists()
        if event_listing.available_nr_tickets > 0:
            reservation = Reservation.objects.create(event = event_listing, user = user)
            event_listing.available_nr_tickets -= 1
            event_listing.save()
            return render(request, 'reservation.html', {'status': 'success', 'has_new_messages': has_new_messages,})
        else:
            return render(request, 'reservation.html', {'status': 'no tickets available', 'has_new_messages': has_new_messages,})

def user_reservations(request):
    user = request.user
    if not user.is_authenticated:
        has_new_messages = False
        return render(request, 'user-reservations.html', {'status': 'not logged in', 'has_new_messages': has_new_messages,})
    else:
        reservations = Reservation.objects.filter(user=user)
        has_new_messages = Message.objects.filter(user=request.user, is_read=False).exists()
        return render(request, 'user-reservations.html', {'status': 'success', 'reservations': reservations, 'has_new_messages': has_new_messages,})

def user_messages(request):
    if not request.user.is_authenticated:
        return redirect('/accounts/login')

    # Obține toate mesajele utilizatorului
    messages = Message.objects.filter(user=request.user)
    messages = messages.order_by('-created_at')
    set_as_read = request.POST.get('set_as_read', '')
    if set_as_read == "True":
        for message in messages:
            message.is_read = True
            message.save()
    has_new_messages = messages.filter(is_read=False).exists()
    return render(request, 'user-messages.html', {'messages': messages, 'has_new_messages': has_new_messages,})

def user_message_mark_read(request):
    user = request.user
    if not user.is_authenticated:
        return redirect('/accounts/login')

    message_id = request.POST['message_id']
    message = Message.objects.get(id=message_id)
    message.update(is_read=True)
    return user_messages(request)


