# Chat 모델
# - ChatRoom: 오픈채팅방(비번O,비번X), 개인채팅방
# - ChatMessage: 메세지를 주고 받는 모델
from django.db import models
from users.models import User
from common.models import CommonModel

class ChatRoom(CommonModel):
    name = models.CharField(max_length=100)

class ChatMessage(CommonModel):
    # 채팅방이 삭제되면 => 메세지도 삭제되어야 하는가?? ㅇㅇ
    room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()

# Room:Message (1:N)
# - Room => Message, Message, Message (O)
# - Message => Room1, Room2, Room3 (X)