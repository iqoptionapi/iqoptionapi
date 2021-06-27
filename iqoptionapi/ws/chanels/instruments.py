from iqoptionapi.ws.chanels.base import Base


class Get_instruments(Base):
    """Class for IQ option buy websocket chanel."""

    # pylint: disable=too-few-public-methods

    name = "sendMessage"

    def __call__(self, types):

        data = {
            "name": "get-instruments",
            "version": "4.0",
            "body": {
                "type": types
            }
        }

        self.send_websocket_request(self.name, data)
