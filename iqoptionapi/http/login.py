"""Module for IQ Option http login resource."""

from iqoptionapi.http.resource import Resource


class Login(Resource):
    """Class for IQ option login resource."""

    # pylint: disable=too-few-public-methods

    url = ""

    def _post(self, data=None, headers=None):
        """Send get request for IQ Option API login http resource.

        :returns: The instance of :class:`requests.Response`.
        """
        return self.api.send_http_request_v2(
            method="POST",
            url="https://auth.iqoption.com/api/v2/login",
            data=data,
            headers=headers,
        )

    def __call__(self, username, password):
        """Method to get IQ Option API login http request.

        :param str username: The username of a IQ Option server.
        :param str password: The password of a IQ Option server.

        :returns: The instance of :class:`requests.Response`.
        """
        data = {"identifier": username, "password": password}

        return self._post(data=data)
