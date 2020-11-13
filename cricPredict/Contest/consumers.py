import json

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from .functions import get_leagues, get_matches


class LeaguesConsumer(WebsocketConsumer):

    def connect(self):
        self.group_name = 'leagues'
        async_to_sync(self.channel_layer.group_add)(self.group_name, self.channel_name)
        self.accept()

    def receive(self, text_data=None, bytes_data=None):
        async_to_sync(self.channel_layer.group_send)(
            self.group_name,
            {
                'type': 'leagues_data',
                'leagues': get_leagues(),
            }
        )

    def disconnect(self, code):
        print("Disconnect")
        async_to_sync(self.channel_layer.group_discard)("league", self.channel_name)

    def leagues_data(self, event):
        leagues = event['leagues']
        self.send(text_data=json.dumps(leagues))


class MatchesConsumer(WebsocketConsumer):

    def connect(self):
        print(self.channel_layer)
        async_to_sync(self.channel_layer.group_add)("match", self.channel_name)
        self.accept()

    def receive(self, text_data=None, bytes_data=None):
        async_to_sync(self.channel_layer.group_send)(
            "match",
            {
                'type': 'matches_data',
                'matches': get_matches(int(text_data)),
            },
        )

    def disconnect(self, code):
        async_to_sync(self.channel_layer.group_discard)("match", self.channel_name)

    def matches_data(self, event):
        matches = event['matches']
        self.send(text_data=json.dumps(matches))
