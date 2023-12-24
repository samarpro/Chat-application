from django.urls import path
from . import consumers


# The code is defining a WebSocket URL pattern for a Django application.
WS_URLPATTERNS = [path("ws/sc/<str:GN>/", consumers.MyConsumer.as_asgi())]
