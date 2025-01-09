from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Place(models.Model):
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.city}, {self.country}"

class EventListing(models.Model):
    CATEGORY_CHOICES = [
        ('concert', 'Concert'),
        ('opera', 'Opera'),
        ('theater', 'Piesa de Teatru'),
        ('standup', 'Stand-Up Comedy'),
        ('ballet', 'Balet'),
    ]

    name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES)
    date = models.DateField()
    price = models.FloatField()
    total_nr_tickets = models.IntegerField()
    available_nr_tickets = models.IntegerField()
    place = models.ForeignKey(Place, on_delete=models.CASCADE, default=1)
    img = models.ImageField(upload_to='pics')
    clicks = models.IntegerField(default=0)
    cancelled = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Reservation(models.Model):
    event = models.ForeignKey(EventListing, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reserved_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Reservation by {self.user.username} for {self.event.name}"

class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(EventListing, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user}: {self.event.name} at {self.created_at}"