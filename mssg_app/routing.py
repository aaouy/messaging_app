from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('ws/chat/<str:room_name>/', consumers.ChatConsumer.as_asgi()),
    path('ws/chatroom/<str:username>/', consumers.ChatRoomConsumer.as_asgi()),
 ]