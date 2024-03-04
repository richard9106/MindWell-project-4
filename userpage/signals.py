"""asign the user to a grup"""
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import Group
from .models import Profile


@receiver(post_save, sender=Profile)
def add_user_to_clients(sender, instance, created, **kawrgs):
    """add the user to a client group"""
    if created:
        try:
            clients = Group.objects.get(name='client')
        except Group.objects.DoesNotExist:
            clients = Group.objects.create(name='client')
        instance.user.group.add(clients)

