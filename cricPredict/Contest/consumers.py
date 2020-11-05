from channels.generic.websocket import WebsocketConsumer
from .functions import get_leagues


class LeaguesConsumer(WebsocketConsumer):

    def connect(self):
        self.accept()
        self.send("HI")

    def receive(self, text_data=None, bytes_data=None):
        self.send(get_leagues())

    def disconnect(self, code):
        pass