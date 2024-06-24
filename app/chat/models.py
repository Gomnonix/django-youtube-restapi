from django.db import models
from users.models import User
from common.models import CommonModel

class ChatRoom(CommonModel):
    name = models.CharField(max_length=100)

class ChatMessage(CommonModel):
    room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()

# Room:Message (1:N)
# - Room => Message, Message, Message (O)
# - Message => Room1, Room2, Room3 (X)