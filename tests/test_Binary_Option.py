import unittest
from unittest.mock import patch, MagicMock
from iqoptionapi.stable_api import IQ_Option

class TestBinaryOption(unittest.TestCase):

    @patch('iqoptionapi.stable_api.IQ_Option.connect')
    @patch('iqoptionapi.stable_api.IQ_Option.check_connect')
    @patch('iqoptionapi.stable_api.IQ_Option.get_all_open_time')
    @patch('iqoptionapi.stable_api.IQ_Option.buy')
    @patch('iqoptionapi.stable_api.IQ_Option.sell_option')
    @patch('iqoptionapi.stable_api.IQ_Option.check_win_v2')
    @patch('iqoptionapi.stable_api.IQ_Option.get_binary_option_detail')
    @patch('iqoptionapi.stable_api.IQ_Option.get_all_profit')
    @patch('iqoptionapi.stable_api.IQ_Option.get_betinfo')
    @patch('iqoptionapi.stable_api.IQ_Option.get_optioninfo')
    @patch('iqoptionapi.stable_api.IQ_Option.change_balance')
    @patch('iqoptionapi.stable_api.IQ_Option.reset_practice_balance')
    def test_binary_option_workflows(self, mock_reset_balance, mock_change_balance,
                                     mock_get_optioninfo, mock_get_betinfo,
                                     mock_get_all_profit, mock_get_binary_option_detail,
                                     mock_check_win_v2, mock_sell_option, mock_buy,
                                     mock_get_all_open_time, mock_check_connect,
                                     mock_connect):
        # Arrange
        mock_connect.return_value = (True, None)
        mock_check_connect.return_value = True
        mock_get_all_open_time.return_value = {
            "turbo": {"EURUSD": {"open": True}},
            "binary": {"EURUSD": {"open": True}}
        }
        mock_buy.side_effect = [(True, 12345), (True, 67890)]
        mock_sell_option.return_value = {"status": "success"}
        mock_check_win_v2.return_value = 0.85
        mock_get_betinfo.return_value = (True, {"id": 67890, "result": "win"})
        mock_get_binary_option_detail.return_value = {"EURUSD": {"turbo": {}}}
        mock_get_all_profit.return_value = {"EURUSD": {"turbo": 0.87}}
        mock_get_optioninfo.return_value = {"options": []}

        # Act
        iq_option = IQ_Option("test@email.com", "password")
        iq_option.connect()
        iq_option.change_balance("PRACTICE")
        iq_option.reset_practice_balance()

        self.assertTrue(iq_option.check_connect())

        all_asset = iq_option.get_all_open_time()
        actives = "EURUSD"

        # Test CALL option
        check_call, id_call = iq_option.buy(1, actives, "call", 1)
        self.assertTrue(check_call)
        self.assertEqual(id_call, 12345)
        iq_option.sell_option(id_call)

        # Test PUT option
        check_put, id_put = iq_option.buy(1, actives, "put", 1)
        self.assertTrue(check_put)
        self.assertEqual(id_put, 67890)
        iq_option.sell_option(id_put)
        iq_option.check_win_v2(id_put)
        
        # Test informational methods
        iq_option.get_binary_option_detail()
        iq_option.get_all_profit()
        is_successful, _ = iq_option.get_betinfo(id_put)
        self.assertTrue(is_successful)
        iq_option.get_optioninfo(10)

        # Assert call counts
        self.assertEqual(mock_buy.call_count, 2)
        self.assertEqual(mock_sell_option.call_count, 2)
        mock_get_betinfo.assert_called_once_with(id_put)
        mock_check_win_v2.assert_called_once_with(id_put)