from django.urls import re_path
from chatapp import consumers

websocket_urlpatterns = [
    # re_path(r'ws/(?P<group>\w+)/$', consumers.ChatConsumer.as_asgi()),
    re_path(r'room/(?P<group>\w+)/$', consumers.ChatConsumer.as_asgi()),
]