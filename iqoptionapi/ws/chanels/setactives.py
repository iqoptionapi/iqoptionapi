"""Module for IQ option setactives websocket chanel."""

from iqoptionapi.ws.chanels.base import Base


class SetActives(Base):
    """Class for IQ option setactives websocket chanel."""

    # pylint: disable=too-few-public-methods

    name = "setActives"

    def __call__(self, actives):
        """Method to send message to setactives websocket chanel.

        :param actives: The list of actives identifiers.
        """
        data = {"actives": actives}
        self.send_websocket_request(self.name, data)
