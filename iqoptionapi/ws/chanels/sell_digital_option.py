import time

from iqoptionapi.ws.chanels.base import Base


class Sell_Digital_Option(Base):
    name = "sendMessage"

    def __call__(self, position_ids):
        """
        :param options_ids: list or int
        """
        if type(position_ids) == list:
            id_list = []
            id_list.append(position_ids)
            position_ids = id_list

            data = {
                "name": "digital-options.close-position-batch",
                "version": "1.0",
                "body": {
                    "position_ids": (position_ids)
                },
            }
        else:
            data = {
                "name": "digital-options.close-position",
                "version": "1.0",
                "body": {
                    "position_id": position_ids
                },
            }
        request_id = int(str(time.time()).split(".")[1])
        self.send_websocket_request(self.name, data, request_id)
