"""Module for IQ option buyback resource."""

from iqoptionapi.http.billing import Billing
from iqoptionapi.http.resource import Resource


class Buyback(Resource):
    """Class for IQ option buyback resource."""

    # pylint: disable=too-few-public-methods

    url = "/".join((Billing.url, "buyback"))

    def _post(self, data=None, headers=None):
        """Send get request for IQ Option API buyback http resource.

        :returns: The instance of :class:`requests.Response`.
        """
        return self.send_http_request("POST", data=data, headers=headers)

    def __call__(self, option_id):
        """Method to get IQ Option API buyback http request.

        :param str option_id: The option identifier.

        :returns: The instance of :class:`requests.Response`.
        """
        data = {"option_id": [option_id]}
        return self._post(data=data)
