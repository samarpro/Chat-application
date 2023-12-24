"""
ASGI config for ChattingApp project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter 
from backend.routing import WS_URLPATTERNS

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ChattingApp.settings')

application = ProtocolTypeRouter({
    'http':get_asgi_application(),
    'websocket': URLRouter(routes=WS_URLPATTERNS)
})

