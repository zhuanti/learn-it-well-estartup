from channels.generic.websocket import WebsocketConsumer
from channels.exceptions import StopConsumer

class ChatConsumer(WebsocketConsumer):
    def websocket_connect(self, message):
        print("there is someone to connect")
        # 客戶端向後端發送websocket連接的請求，自動觸發
        # 服務端允許
        self.accept()

        # 給客戶端發消息
        self.send("hello client")

    def websocket_receive(self, message):
        # 瀏覽器基於websocket向後端發送數據，自動觸發接收消息
        text = message['text']
        print("get message -->", text)

        if text == "close":
            # 服務端主動關閉連接，給客戶端斷開連接的訊息
            self.close()
            # raise StopConsumer() # 如果服務端斷開連接時，執行websocket_disconnect異常，那麼websocket_disconnect方法將不在執行
            return

        res = "{}".format(text)
        # res = "{}sb".format(text) # 傳回的字串，後面都加sb
        self.send(res)

        # self.send("不要回復")

        # self.close 服務端主動斷開連接

    def websocket_disconnect(self, message):
        # 客戶端與服務端斷開連接結時，自動觸發。(不論誰主動)
        print("client disconnect")
        # 服務端也同意雙方斷開連接
        raise StopConsumer()