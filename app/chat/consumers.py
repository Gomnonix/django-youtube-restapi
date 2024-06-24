from channels.generic.websocket import AsyncWebsocketConsumer
import json

class ChatConsumer(AsyncWebsocketConsumer):
    # 소켓 연결
    async def connect(self):
        self.room_id = self.scope['url_route']['kwargs']['room_id']
        self.room_group_name = 'chat_'+str(self.room_id)

        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        msg = text_data_json.get('message')
            
        await self.channel_layer.group_send(self.room_group_name, {
            'type': 'chat_message',
            'message': msg
        })

	# 연결 해제 메서드: 클라이언트의 웹소켓 연결이 끊어졌을 때 호출됩니다.
	# group_discard: 클라이언트를 채팅방 그룹에서 제거합니다. 이를 통해 더 이상 메시지를 받지 않게 됩니다.        
    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def chat_message(self, event):
        msg = event['message']

        await self.send(text_data=json.dumps({
            'type': 'chat.message',
            'message': msg,
        }))