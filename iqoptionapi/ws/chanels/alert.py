from iqoptionapi.ws.chanels.base import Base
from random import randint


class CreateAlert(Base):
    name = "sendMessage"

    def __call__(self, active_id, value):
        data = {
            "name": "create-alert",
            "version": "1.0",
            "body": {
                "activations": 1,
                "asset_id": int(active_id),
                "instrument_type": "turbo",
                "type": "price",
                "value": float(value)
            }
        }
        request_id = str(randint(0, 100000))
        self.send_websocket_request(self.name, data, request_id)
        return request_id


class DeleteAlert(Base):
    name = "sendMessage"

    def __call__(self, alert_id):
        data = {
            "name": "delete-alert",
            "version": "1.0",
            "body": {
                "id": int(alert_id),
            }
        }
        self.send_websocket_request(self.name, data)


class GetAlerts(Base):
    name = "sendMessage"

    def __call__(self):
        data = {
            "name": "get-alerts",
            "version": "1.0",
            "body": {
                "asset_id": 0,
                "type": ""
            }
        }
        self.send_websocket_request(self.name, data)
