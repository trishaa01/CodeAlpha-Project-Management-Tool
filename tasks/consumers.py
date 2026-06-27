import json
from channels.generic.websocket import AsyncWebsocketConsumer


class ProjectConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.project_id = self.scope['url_route']['kwargs']['project_id']
        self.group_name = f'project_{self.project_id}'

        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        data = json.loads(text_data)
        await self.channel_layer.group_send(
            self.group_name,
            {
                'type': 'task_update',
                'task_id': data['task_id'],
                'status': data['status'],
                'title': data['title'],
            }
        )

    async def task_update(self, event):
        await self.send(text_data=json.dumps({
            'type': 'task_update',
            'task_id': event['task_id'],
            'status': event['status'],
            'title': event['title'],
        }))


class TaskConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.task_id = self.scope['url_route']['kwargs']['task_id']
        self.group_name = f'task_{self.task_id}'

        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        data = json.loads(text_data)
        await self.channel_layer.group_send(
            self.group_name,
            {
                'type': 'new_comment',
                'comment': data['comment'],
                'author': data['author'],
                'time': data['time'],
            }
        )

    async def new_comment(self, event):
        await self.send(text_data=json.dumps({
            'type': 'new_comment',
            'comment': event['comment'],
            'author': event['author'],
            'time': event['time'],
        }))