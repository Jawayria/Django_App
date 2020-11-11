from channels.routing import URLRouter
from django.urls import path, re_path
from .consumers import LeaguesConsumer, MatchesConsumer, GroupsConsumer
'''''
websocket_urlpatterns = [
    re_path(r"^leagues-data/$", LeaguesConsumer.as_asgi()),
    re_path(r"^matches-data/$", MatchesConsumer.as_asgi()),
    re_path(r"^groups-data/$", GroupsConsumer.as_asgi()),
]
'''''

from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.conf.urls import url
from . import consumers

websocket_urlpatterns = [
    re_path(r"^leagues-data/$", LeaguesConsumer),
    re_path(r"^matches-data/$", MatchesConsumer),
    re_path(r"^groups-data/$", GroupsConsumer),
]
application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(
        URLRouter(
            websocket_urlpatterns
        )
    ),
}
)