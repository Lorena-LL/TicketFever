from django.contrib import admin
from .models import EventListing, Place, Reservation, Message

# Register your models here.

admin.site.register(EventListing)
admin.site.register(Place)
admin.site.register(Reservation)
admin.site.register(Message)
