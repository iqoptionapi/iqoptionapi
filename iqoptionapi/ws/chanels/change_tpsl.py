# python

from iqoptionapi.ws.chanels.base import Base


class Change_Tpsl(Base):
    name = "sendMessage"

    def __call__(
        self,
        ID_Name,
        ID,
        stop_lose_kind,
        stop_lose_value,
        take_profit_kind,
        take_profit_value,
        use_trail_stop,
    ):
        data = {
            "name": "change-tpsl",
            "version": "2.0",
            "body": {
                ID_Name: ID,
                "stop_lose_kind": stop_lose_kind,
                "stop_lose_value": stop_lose_value,
                "take_profit_kind": take_profit_kind,
                "take_profit_value": take_profit_value,
                "use_trail_stop": use_trail_stop,
                "extra": {
                    "stop_lose_kind": stop_lose_kind,
                    "take_profit_kind": take_profit_kind,
                },
            },
        }
        self.send_websocket_request(self.name, data)
