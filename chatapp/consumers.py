from channels.generic.websocket import WebsocketConsumer
from channels.exceptions import StopConsumer
from asgiref.sync import async_to_sync
from django.db.models.functions import datetime


class ChatConsumer(WebsocketConsumer):
    # 客戶端向後端發送websocket連接的請求，自動觸發
    def websocket_connect(self, message):

        # 服務端允許連接
        self.accept()

        # 獲取討論室號碼(在路由匹配中的)
        group = self.scope['url_route']['kwargs'].get("group")

        # 將這個客戶加入某個地方 (內存 or redis)
        async_to_sync(self.channel_layer.group_add)(group, self.channel_name) # 將異步改為同步

    def websocket_receive(self, message):
        # 瀏覽器基於websocket向後端發送數據，自動觸發接收消息

        # 獲取討論室號碼(在路由匹配中的)
        group = self.scope['url_route']['kwargs'].get("group")

        # 通知組內所有的使用者，執行xx_oo方法，在此方法中可自訂
        async_to_sync(self.channel_layer.group_send)(group, {"type": "xx.oo", 'message': message})

    def xx_oo(self, event):
        
        text = event['message']['text']
        # # 給channel_layer裡整個組的人發送
        # self.send(text)

        # datetime_str = datetime.datetime.now().strftime('%H:%M:%S')
        # res = datetime_str + "　{}".format(text)
        res = text
        # 給channel_layer裡整個組的人發送
        self.send(res)

    def websocket_disconnect(self, message):
        # 獲取討論室號碼(在路由匹配中的)
        group = self.scope['url_route']['kwargs'].get("group")

        # 客戶端與服務端斷開連接結時，自動觸發。(不論誰主動)
        async_to_sync(self.channel_layer.group_discard)(group, self.channel_name)
        # 服務端也同意雙方斷開連接
        raise StopConsumer()