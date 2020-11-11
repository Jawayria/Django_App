import json

from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.db.models.signals import post_save
from django.dispatch import receiver

from .functions import get_leagues
from .models import League, Match


def data(event):
    '''
    Call back function to send message to the browser
    '''
    print("CALLBACK")
    leagues = event['text']
    channel_layer = get_channel_layer()
    # Send message to WebSocket
    async_to_sync(channel_layer.send)(text_data=json.dumps(
        leagues
    ))


@receiver(post_save, sender=League, dispatch_uid='push_leagues_data')
def push_leagues_data(sender, instance, **kwargs):

    print("SIGNAL")
    group_name = 'leagues'
    user = instance.owner
    group_name = 'leagues-{}'.format(user.username)
    leagues = {
        get_leagues()
    }

    channel_layer = get_channel_layer()

    async_to_sync(channel_layer.group_send)(
        group_name,
        {
            'type': 'data',
            'text': leagues
        }
    )

