from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from .models import League, Match


def push_new_leagues(sender, instance, **kwargs):
    print("generating signal")
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.send)(text_data="send signal")
