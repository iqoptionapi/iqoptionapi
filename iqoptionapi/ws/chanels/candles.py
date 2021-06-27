"""Module for IQ option candles websocket chanel."""

from iqoptionapi.ws.chanels.base import Base


class GetCandles(Base):
    """Class for IQ option candles websocket chanel."""

    # pylint: disable=too-few-public-methods

    name = "sendMessage"

    def __call__(self, active_id, interval, count, endtime):
        """Method to send message to candles websocket chanel.

        :param active_id: The active/asset identifier.
        :param duration: The candle duration (timeframe for the candles).
        :param amount: The number of candles you want to have
        """
        # thank SeanStayn share new request
        # https://github.com/n1nj4z33/iqoptionapi/issues/88
        data = {
            "name": "get-candles",
            "version": "2.0",
            "body": {
                "active_id": int(active_id),
                # time size sample:if interval set 1 mean get time 0~1 candle
                "size": interval,
                # int(self.api.timesync.server_timestamp),
                "to": int(endtime),
                # get how many candle
                "count": count,
                "": active_id,
            },
        }

        self.send_websocket_request(self.name, data)
