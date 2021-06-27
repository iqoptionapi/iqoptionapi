from iqoptionapi.ws.chanels.base import Base


class Sell_Option(Base):
    name = "sendMessage"

    def __call__(self, options_ids):
        """
        :param options_ids: list or int
        """
        if type(options_ids) != list:
            id_list = []
            id_list.append(options_ids)
            options_ids = id_list

        data = {
            "name": "sell-options",
            "version": "2.0",
            "body": {
                "options_ids": (options_ids)
            },
        }

        self.send_websocket_request(self.name, data)
