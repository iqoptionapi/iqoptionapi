import unittest
from unittest.mock import patch, MagicMock
import time
from iqoptionapi.stable_api import IQ_Option

class TestDigitalOption(unittest.TestCase):

    @patch('iqoptionapi.stable_api.IQ_Option.connect')
    @patch('iqoptionapi.stable_api.IQ_Option.check_connect')
    @patch('iqoptionapi.stable_api.IQ_Option.get_digital_underlying_list_data')
    @patch('iqoptionapi.stable_api.IQ_Option.subscribe_strike_list')
    @patch('iqoptionapi.stable_api.IQ_Option.get_realtime_strike_list')
    @patch('iqoptionapi.stable_api.IQ_Option.buy_digital_spot')
    @patch('iqoptionapi.stable_api.IQ_Option.check_win_digital_v2')
    @patch('iqoptionapi.stable_api.IQ_Option.unsubscribe_strike_list')
    def test_digital_option_workflows(self, mock_unsubscribe, mock_check_win,
                                      mock_buy_digital, mock_get_realtime,
                                      mock_subscribe, mock_get_underlying,
                                      mock_check_connect, mock_connect):
        # Arrange
        mock_connect.return_value = (True, None)
        mock_check_connect.return_value = True
        mock_get_underlying.return_value = {"underlying": [{"name": "EURUSD"}]}
        mock_get_realtime.return_value = {
            '1.127100': {
                'call': {'profit': 100, 'id': 'doEURUSD...'},
                'put': {'profit': 90, 'id': 'doEURUSD...'}
            }
        }
        mock_buy_digital.return_value = (True, 98765)
        mock_check_win.return_value = (True, 85.0)

        # Act
        iq_option = IQ_Option("test@email.com", "password")
        iq_option.connect()

        self.assertTrue(iq_option.check_connect())

        actives = "EURUSD"
        duration = 1
        amount = 100
        action = "call"

        # Test digital option workflow
        iq_option.subscribe_strike_list(actives, duration)

        strike_list = iq_option.get_realtime_strike_list(actives, duration)
        self.assertIsInstance(strike_list, dict)

        check_buy, order_id = iq_option.buy_digital_spot(actives, amount, action, duration)
        self.assertTrue(check_buy)
        self.assertEqual(order_id, 98765)

        is_closed, win_amount = iq_option.check_win_digital_v2(order_id)
        self.assertTrue(is_closed)
        self.assertEqual(win_amount, 85.0)

        iq_option.unsubscribe_strike_list(actives, duration)

        # Assert
        mock_subscribe.assert_called_once_with(actives, duration)
        mock_buy_digital.assert_called_once_with(actives, amount, action, duration)
        mock_check_win.assert_called_once_with(order_id)
        mock_unsubscribe.assert_called_once_with(actives, duration)