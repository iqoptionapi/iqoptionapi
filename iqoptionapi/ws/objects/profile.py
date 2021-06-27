"""Module for IQ Option Profile websocket object."""
from iqoptionapi.ws.objects.base import Base


class Profile(Base):
    """Class for IQ Option Profile websocket object."""

    def __init__(self):
        super(Profile, self).__init__()
        self.__name = "profile"
        self.__skey = None
        self.__balance = None
        self.__balance_id = None
        self.__balances = None
        self.__msg = None
        self.__currency = None
        self.__minimum_amount = 1
        self.__balance_type = None
        self.__currency_char = None
        self.__time_zone = -3

    @property
    def skey(self):
        """Property to get skey value.

        :returns: The skey value.
        """
        return self.__skey

    @skey.setter
    def skey(self, skey):
        """Method to set skey value."""
        self.__skey = skey

    # ----------------------------------------------------------------
    @property
    def balance(self):
        """Property to get balance value.

        :returns: The balance value.
        """
        return self.__balance

    @balance.setter
    def balance(self, balance):
        """Method to set balance value."""
        self.__balance = balance

    # ---------------------------------------------------------------------
    @property
    def balance_id(self):
        """Property to get balance value.

        :returns: The balance value.
        """
        return self.__balance_id

    @balance_id.setter
    def balance_id(self, balance_id):
        """Method to set balance value."""
        self.__balance_id = balance_id

    # ------------------------------------------------------------------------
    @property
    def balance_type(self):
        """Property to get balance value.

        :returns: The balance value.
        """
        return self.__balance_type

    @balance_type.setter
    def balance_type(self, balance_type):
        """Method to set balance value."""
        self.__balance_type = balance_type

    # ----------------------------------------
    @property
    def balances(self):
        """Property to get balance value.

        :returns: The balance value.
        """
        return self.__balances

    @balances.setter
    def balances(self, balances):
        """Method to set balance value."""
        self.__balances = balances

    # ------------
    @property
    def msg(self):
        return self.__msg

    @msg.setter
    def msg(self, msg):
        self.__msg = msg

    # ------------
    @property
    def currency(self):
        return self.__currency

    @currency.setter
    def currency(self, currency):
        self.__currency = currency
        if self.__currency.upper() == "BRL":
            self.__minimum_amount = 2

    @property
    def minimum_amount(self):
        return self.__minimum_amount

    # ------------
    @property
    def currency_char(self):
        return self.__currency_char

    @currency_char.setter
    def currency_char(self, currency_char):
        self.__currency_char = currency_char

    # ------------
    @property
    def time_zone(self):
        return self.__time_zone

    @time_zone.setter
    def time_zone(self, time_zone):
        self.__time_zone = int(time_zone / 60)
