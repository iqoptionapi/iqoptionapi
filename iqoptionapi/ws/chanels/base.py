"""Module for base IQ Option base websocket chanel."""
import time


class Base(object):
    """Class for base IQ Option websocket chanel."""

    # pylint: disable=too-few-public-methods

    def __init__(self, api):
        """
        :param api: The instance of :class:`IQOptionAPI
            <iqoptionapi.api.IQOptionAPI>`.
        """
        self.api = api

    def send_websocket_request(self, name, msg, request_id=""):
        """Send request to IQ Option server websocket.

        :param str name: The websocket chanel name.
        :param dict msg: The websocket chanel msg.

        :returns: The instance of :class:`requests.Response`.
        """
        if request_id == "":
            request_id = int(str(time.time()).split(".")[1])
        return self.api.send_websocket_request(name, msg, request_id)
