from channels.generic.websocket import AsyncWebsocketConsumer
import json
from asgiref.sync import sync_to_async

class MachineConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.machine_slug = self.scope['url_route']['kwargs']['machine_slug']
        self.machine_group_name = 'machine_%s' % self.machine_slug
        
        await self.channel_layer.group_add(
            self.machine_group_name,
            self.channel_name
        )
        
        await self.accept()
        
    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.machine_group_name,
            self.channel_name
        )
        
    async def receive(self, text_data):
        text_data_json = (text_data)
        message = text_data_json
        
        await self.channel_layer.group_send(
            self.machine_group_name,
            {
                'type': 'machine_message',
                'message': message
            }
        )
        
    async def machine_message(self, event):
        message = event['message']
        
        await self.send(text_data=json.dumps({
            'message': message
        }))