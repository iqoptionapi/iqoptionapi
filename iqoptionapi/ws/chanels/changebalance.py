"""Module for IQ Option buyV2 websocket chanel."""

from iqoptionapi.ws.chanels.base import Base


class Changebalance(Base):
    """Class for IQ option buy websocket chanel."""

    # pylint: disable=too-few-public-methods

    name = "api_profile_changebalance"

    def __call__(self, balance_id):
        """Method to send message to buyv2 websocket chanel.

        :param price: The buying price.
        :param active: The buying active.
        :param option: The buying option.
        :param direction: The buying direction.
        """

        data = {"balance_id": balance_id}

        self.send_websocket_request(self.name, data)
