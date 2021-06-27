"""Module for IQ Option http loginv2 resource."""

from iqoptionapi.http.login import Login


class Loginv2(Login):
    """Class for IQ option loginv2 resource."""

    # pylint: disable=too-few-public-methods

    url = "/".join((Login.url, "v2"))

    def __init__(self, api):
        super(Loginv2, self).__init__(api)
