"""Module for IQ option billing resource."""

from iqoptionapi.http.resource import Resource


class Billing(Resource):
    """Class for IQ option billing resource."""

    # pylint: disable=too-few-public-methods

    url = "billing"
