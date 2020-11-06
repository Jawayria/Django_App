from asgiref.sync import async_to_sync
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from channels.layers import get_channel_layer
from .models import League, Match


@receiver(post_save, sender=League)
def push_new_leagues(sender, instance, **kwargs):
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.send)(text_data="send signal")
