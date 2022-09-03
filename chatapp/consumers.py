from channels.generic.websocket import WebsocketConsumer
from channels.exceptions import StopConsumer

class ChatConsumer(WebsocketConsumer):
    def websocket_connect(self, message):
        # 客戶端向後端發送websocket連接的請求，自動觸發
        # 服務端允許
        self.accept()

    def websocket_receive(self, message):
        # 瀏覽器基於websocket向後端發送數據，自動觸發接收消息
        print(message)
        self.send("不要回復")

        # self.close 服務端主動斷開連接

    def websocket_disconnect(self, message):
        # 客戶端與服務端斷開連接結時，自動觸發。
        print("斷開連接")
        raise StopConsumer()