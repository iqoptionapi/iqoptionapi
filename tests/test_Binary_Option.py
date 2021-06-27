import unittest
import os
from iqoptionapi.stable_api import IQ_Option
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s')

email = os.getenv("email")
password = os.getenv("password")


class TestBinaryOption(unittest.TestCase):
    def test_binary_option(self):
        # login
        I_want_money = IQ_Option(email, password)
        I_want_money.change_balance("PRACTICE")
        I_want_money.reset_practice_balance()
        self.assertEqual(I_want_money.check_connect(), True)
        # start test binary option
        ALL_Asset = I_want_money.get_all_open_time()
        if ALL_Asset["turbo"]["EURUSD"]["open"]:
            ACTIVES = "EURUSD"
        else:
            ACTIVES = "EURUSD-OTC"
        Money = 1
        ACTION_call = "call"  # or "put"
        expirations_mode = 1
        check_call, id_call = I_want_money.buy(Money, ACTIVES, ACTION_call,
                                               expirations_mode)
        self.assertTrue(check_call)
        self.assertTrue(type(id_call) is int)
        I_want_money.sell_option(id_call)

        ACTION_call = "put"
        check_put, id_put = I_want_money.buy(Money, ACTIVES, ACTION_call,
                                             expirations_mode)
        self.assertTrue(check_put)
        self.assertTrue(type(id_put) is int)
        I_want_money.sell_option(id_put)
        I_want_money.check_win_v2(id_put)

        I_want_money.get_binary_option_detail()

        I_want_money.get_all_profit()

        isSuccessful, dict = I_want_money.get_betinfo(id_put)
        self.assertTrue(isSuccessful)
        I_want_money.get_optioninfo(10)
