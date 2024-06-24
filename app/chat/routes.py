from django.urls import re_path, path
from .consumers import ChatConsumer

websocket_urlpatterns = [
    # re_path(r'ws/chat/(?P<room_id>\d+)/'), # URL과 VIEW를 연결하는데, 정규 표현식을 사용한 경우
    path('ws/chat/<int:room_id>/', ChatConsumer.as_asgi())
]