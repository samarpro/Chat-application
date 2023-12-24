from channels import layers
from channels.consumer import SyncConsumer
from channels.exceptions import StopConsumer
from asgiref.sync import async_to_sync
from backend.models import ChatDB,GroupDB

# since consumers are classes that inherits property from above class

class MyConsumer(SyncConsumer):
    def websocket_connect(self,e):
        self.group_name = self.scope['url_route']['kwargs']['GN']
        async_to_sync(self.channel_layer.group_add)(self.group_name,self.channel_name) #type:ignore
        self.send({
            'type':'websocket.accept',
        })

    def websocket_receive(self,e):
        NewChat = ChatDB.objects.create(content =e['text'],Group=GroupDB.objects.filter(Name = self.group_name).first())
        NewChat.save()
        async_to_sync (self.channel_layer.group_send)(self.group_name,{ #type:ignore
            'type':'websocket.MsgSend',
            'message':e['text'],
        })
    
    def websocket_MsgSend(self,e):
        self.send({
            'type':'websocket.send',
            'text': e['message'],
        })

    def websocket_disconnect(self,e):
        print("Connection Broken: ", e)
        raise StopConsumer