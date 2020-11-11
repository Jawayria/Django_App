import json

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer, SyncConsumer
from requests import Response

from Groups.models import Group
from Groups.serializers import ExtendedGroupSerializer
from .functions import get_leagues, get_matches


class LeaguesConsumer(WebsocketConsumer):

    def connect(self):
        print("Connect")
        print(self.scope["user"])
        user = self.scope["user"]
        self.group_name = 'leagues-{}'.format(user.username)
        async_to_sync(self.channel_layer.group_add)(self.group_name, self.channel_name)
        self.accept()

    def receive(self, text_data=None, bytes_data=None):
        print("RECEIVER")
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
        # Send message to WebSocket
        self.send(text_data=json.dumps(matches))


class GroupsConsumer(WebsocketConsumer):

    def connect(self):
        self.accept()

    def receive(self, text_data=None, bytes_data=None):
        user_groups = Group.objects.filter(users__in=[int(text_data)])
        user_group_ids = user_groups.values('id')
        public_groups = Group.objects.filter(privacy='public').exclude(id__in=user_group_ids)

        public_groups_serializer = ExtendedGroupSerializer(public_groups, many=True)
        joined_groups_serializer = ExtendedGroupSerializer(user_groups, many=True)

        self.send(json.dumps(
            {"public_groups": public_groups_serializer.data, "joined_groups": joined_groups_serializer.data}))

    def disconnect(self, code):
        pass
