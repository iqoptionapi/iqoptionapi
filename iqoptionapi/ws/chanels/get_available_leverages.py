from iqoptionapi.ws.chanels.base import Base


class Get_available_leverages(Base):
    name = "sendMessage"

    def __call__(self, instrument_type, actives):
        data = {
            "name": "get-available-leverages",
            "version": "2.0",
            "body": {
                "instrument_type": instrument_type,
                "actives": [actives]
            },
        }
        self.send_websocket_request(self.name, data)
