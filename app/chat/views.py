from rest_framework.views import APIView
from .models import ChatRoom, ChatMessage
from .serializers import ChatRoomSerializer, ChatMessageSerializer
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render


def show_html(request):
    return render(request, 'index.html')

# ChatRoom
# [GET]: 전체 채팅방을 조회
# [POST]: 채팅방 생성
class ChatRoomList(APIView):
    def get(self, request):
        chatrooms = ChatRoom.objects.all()
        # 장고 객체 -> JSON (직렬화)
        serializer = ChatRoomSerializer(chatrooms, many=True)        

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        user_data = request.data
        serializer = ChatRoomSerializer(data=user_data) # 역직렬화 (json to django objects)        

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.erros, status=status.HTTP_400_BAD_REQUEST)

# ChatMessage
# [GET]: 특정 채팅방의 채팅 내역 -> 카카오 채팅 서버(채팅 내역을 로컬에 저장)
# [POST]: 채팅 메세지 생성
from django.shortcuts import get_object_or_404

class ChatMessageList(APIView):
    def get(self, request, room_id):
        chatroom = get_object_or_404(ChatRoom, id=room_id)
        messages = ChatMessage.objects.filter(room=chatroom) # django objects
        # 직렬화
        serializer = ChatMessageSerializer(messages, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, room_id):
        chatroom = get_object_or_404(ChatRoom, id=room_id)
        serializer = ChatMessageSerializer(data=request.data) # json -> objects

        if serializer.is_valid():
            # serializer.save(chatroom)
            serializer.save(room=chatroom, sender=request.user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)