from django.urls import path, re_path
from .consumers import LeaguesConsumer, MatchesConsumer
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack

websocket_urlpatterns = [
    re_path(r"^leagues-data/$", LeaguesConsumer),
    re_path(r"^matches-data/$", MatchesConsumer),
]
application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(
        URLRouter(
            websocket_urlpatterns
        )
    ),
}
)