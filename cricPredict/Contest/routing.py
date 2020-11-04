from channels.routing import URLRouter
from django.urls import path
from .consumers import LeaguesConsumer


URLRouter([
    path("/leagues_data", LeaguesConsumer.as_asgi()),
])
