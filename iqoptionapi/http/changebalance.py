"""Module for IQ option changebalance resource."""

from iqoptionapi.http.profile import Profile
from iqoptionapi.http.resource import Resource


class Changebalance(Resource):
    """Class for IQ option changebalance resource."""

    # pylint: disable=too-few-public-methods

    url = "/".join((Profile.url, "changebalance"))

    def _post(self, data=None, headers=None):
        """Send get request for IQ Option API changebalance http resource.

        :returns: The instance of :class:`requests.Response`.
        """
        return self.send_http_request("POST", data=data, headers=headers)

    def __call__(self, balance_id):
        """Method to get IQ Option API changebalance http request.

        :param str balance_id: The balance identifier.

        :returns: The instance of :class:`requests.Response`.
        """
        data = {"balance_id": balance_id}
        return self._post(data)
