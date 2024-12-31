from datetime import datetime

from django.db import models
from django.db.models import CharField


# Create your models here.


class EventListing(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(max_length=100)
    date = models.DateField()
    price = models.FloatField()
    total_nr_tickets = models.IntegerField()
    available_nr_tickets = models.IntegerField()
    organiser_id = models.IntegerField()
    place_id = models.IntegerField()
    img = models.ImageField(upload_to='pics')
