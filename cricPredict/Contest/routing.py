from channels.routing import URLRouter
from django.urls import path, re_path
from .consumers import LeaguesConsumer, MatchesConsumer


websocket_urlpatterns = [
    re_path(r"^leagues-data/$", LeaguesConsumer.as_asgi()),
    re_path(r"^matches-data/$", MatchesConsumer.as_asgi()),
]
