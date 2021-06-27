"""Module for IQ Option http token resource."""

from iqoptionapi.http.auth import Auth
from iqoptionapi.http.resource import Resource


class Token(Resource):
    """Class for IQ Option http token resource."""

    # pylint: disable=too-few-public-methods

    url = "/".join((Auth.url, "token"))

    def __init__(self, api):
        super(Token, self).__init__(api)

    def _get(self):
        """Send get request for IQ Option API token http resource.

        :returns: The instance of :class:`requests.Response`.
        """
        return self.send_http_request("GET")

    def __call__(self):
        """Method to get IQ Option API token http request.

        :returns: The instance of :class:`requests.Response`.
        """
        return self._get()
