from iqoptionapi.ws.chanels.base import Base


class Get_order(Base):
    name = "sendMessage"

    def __call__(self, order_id):
        data = {"name": "get-order", "body": {"order_id": int(order_id)}}
        self.send_websocket_request(self.name, data)


# {"name":"sendMessage","request_id":"140","msg":{"name":"get-order","version":"1.0","body":{"order_id":664130181}}}
