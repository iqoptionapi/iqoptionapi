"""Module for IQ Option Candles websocket object."""

from iqoptionapi.ws.objects.base import Base


class ListInfoData(Base):
    """Class for IQ Option Candles websocket object."""

    def __init__(self):
        super(ListInfoData, self).__init__()
        self.__name = "listInfoData"
        self.listinfodata_dict = {}

    # --------------------
    def set(self, win, game_state, id_number):
        self.listinfodata_dict[id_number] = {
            "win": win,
            "game_state": game_state
        }

    def delete(self, id_number):
        del self.listinfodata_dict[id_number]

    def get(self, id_number):
        return self.listinfodata_dict[id_number]
