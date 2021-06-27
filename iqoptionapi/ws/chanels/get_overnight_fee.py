from iqoptionapi.ws.chanels.base import Base


class Get_overnight_fee(Base):
    name = "sendMessage"

    def __call__(self, instrument_type, active_id):
        data = {
            "name": "get-overnight-fee",
            "version": "1.0",
            "body": {
                "user_group_id": 1,
                "instrument_type": instrument_type,
                "active_id": active_id,
            },
        }
        self.send_websocket_request(self.name, data)
