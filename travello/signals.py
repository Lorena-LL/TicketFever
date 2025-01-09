from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import EventListing, Message, Reservation

@receiver(pre_save, sender=EventListing)
def handle_event_cancellation(sender, instance, **kwargs):
    if instance.pk:  # Dacă instanța există deja în baza de date
        previous_event = EventListing.objects.get(pk=instance.pk)
        # Verificăm dacă `cancelled` trece de la False la True
        if (not previous_event.cancelled) and instance.cancelled:
            # Găsim utilizatorii care au rezervări pentru evenimentul respectiv
            reservations = Reservation.objects.filter(event=instance)
            for reservation in reservations:
                # Creăm un mesaj pentru fiecare utilizator
                Message.objects.create(
                    user=reservation.user,
                    event=instance,
                    text=f"Evenimentul '{instance.name}' a fost anulat."
                )
