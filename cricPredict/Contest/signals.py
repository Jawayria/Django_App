import logging

from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.db.models.signals import post_save
from django.dispatch import receiver

from .functions import get_leagues, get_matches
from .models import League, Match

logger = logging.getLogger(__name__)


@receiver(post_save, sender=League, dispatch_uid='push_leagues_data')
def push_leagues_data(sender, instance, **kwargs):
    logger.debug("received post save signal for league")

    group_name = 'leagues'
    leagues = get_leagues()
    channel_layer = get_channel_layer()

    async_to_sync(channel_layer.group_send)(
        group_name,
        {
            'type': 'leagues_data',
            'leagues': leagues
        }
    )


@receiver(post_save, sender=Match, dispatch_uid='push_leagues_data')
def push_matches_data(sender, instance, **kwargs):
    logger.debug("received post save signal for league")

    group_name = 'matches'
    matches = get_matches(instance.league_id)
    channel_layer = get_channel_layer()

    async_to_sync(channel_layer.group_send)(
        group_name,
        {
            'type': 'matches_data',
            'matches': matches
        }
    )
