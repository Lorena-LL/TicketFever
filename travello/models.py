from django.db import models

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

    def __str__(self):
        return self.name

