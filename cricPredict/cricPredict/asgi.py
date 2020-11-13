"""
ASGI config for cricPredict project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""
import os

import django
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from Contest.routing import websocket_urlpatterns

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cricPredict.settings')
django.setup()

application = ProtocolTypeRouter({
  "websocket": AuthMiddlewareStack(
        URLRouter(websocket_urlpatterns)
    ),
  # Just HTTP for now. (We can add other protocols later.)
})
