from iqoptionapi.ws.chanels.base import Base


class ChangeAutoMarginCall(Base):
    name = "sendMessage"

    def __call__(self, ID_Name, ID, auto_margin_call):
        data = {
            "name": "change-auto-margin-call",
            "version": "2.0",
            "body": {
                ID_Name: ID,
                "auto_margin_call": bool(auto_margin_call)
            },
        }
        self.send_websocket_request(self.name, data)
