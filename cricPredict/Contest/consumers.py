import json

from channels.generic.websocket import WebsocketConsumer
from requests import Response

from .functions import get_leagues, get_matches


class LeaguesConsumer(WebsocketConsumer):

    def connect(self):
        self.accept()

    def receive(self, text_data=None, bytes_data=None):
        self.send(json.dumps(get_leagues()))

    def disconnect(self, code):
        pass


class MatchesConsumer(WebsocketConsumer):

    def connect(self):
        self.accept()

    def receive(self, text_data=None, bytes_data=None):
        self.send(json.dumps(get_matches(int(text_data))))

    def disconnect(self, code):
        pass
