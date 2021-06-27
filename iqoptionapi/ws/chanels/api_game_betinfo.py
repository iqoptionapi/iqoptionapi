import logging

from iqoptionapi.ws.chanels.base import Base


class Game_betinfo(Base):
    name = "api_game_betinfo"

    def __call__(self, id_number_list):
        data = {"currency": "USD"}
        if type(id_number_list) is list:
            for idx, val in enumerate(id_number_list):
                data["id[" + str(idx) + "]"] = int(val)
        elif id_number_list is None:
            logging.error(
                "**error** Game_betinfo can not input None type,please input buy id"
            )
        else:
            data["id[0]"] = int(id_number_list)
        self.send_websocket_request(self.name, data)
