import unittest
from unittest.mock import patch
import time
from iqoptionapi.stable_api import IQ_Option

class TestCandle(unittest.TestCase):

    @patch('iqoptionapi.stable_api.IQ_Option.connect')
    @patch('iqoptionapi.stable_api.IQ_Option.check_connect')
    @patch('iqoptionapi.stable_api.IQ_Option.get_all_open_time')
    @patch('iqoptionapi.stable_api.IQ_Option.get_candles')
    @patch('iqoptionapi.stable_api.IQ_Option.start_candles_stream')
    @patch('iqoptionapi.stable_api.IQ_Option.get_realtime_candles')
    @patch('iqoptionapi.stable_api.IQ_Option.stop_candles_stream')
    @patch('iqoptionapi.stable_api.IQ_Option.change_balance')
    @patch('iqoptionapi.stable_api.IQ_Option.reset_practice_balance')
    def test_candle_workflows(self, mock_reset_balance, mock_change_balance,
                              mock_stop_candles, mock_get_realtime, mock_start_candles,
                              mock_get_candles, mock_get_all_open_time,
                              mock_check_connect, mock_connect):
        # Arrange
        mock_connect.return_value = (True, None)
        mock_check_connect.return_value = True
        mock_get_all_open_time.return_value = {
            "turbo": {"EURUSD": {"open": True}},
            "binary": {"EURUSD": {"open": True}}
        }
        mock_get_candles.return_value = [{"id": 1, "from": time.time(), "to": time.time()}]
        mock_get_realtime.return_value = {60: {time.time(): {"close": 1.1}}}

        # Act
        iq_option = IQ_Option("test@email.com", "password")
        iq_option.connect()
        iq_option.change_balance("PRACTICE")
        iq_option.reset_practice_balance()

        self.assertTrue(iq_option.check_connect())

        all_asset = iq_option.get_all_open_time()
        actives = "EURUSD"

        # Test historical candles
        candles = iq_option.get_candles(actives, 60, 100, time.time())
        self.assertIsInstance(candles, list)
        self.assertGreater(len(candles), 0)

        # Test realtime candles
        size = "all"
        iq_option.start_candles_stream(actives, size, 10)
        realtime_candles = iq_option.get_realtime_candles(actives, size)
        self.assertIsInstance(realtime_candles, dict)

        iq_option.stop_candles_stream(actives, size)

        # Assert
        mock_connect.assert_called_once()
        mock_change_balance.assert_called_once_with("PRACTICE")
        mock_get_candles.assert_called_once()
        mock_start_candles.assert_called_once_with(actives, size, 10)
        mock_get_realtime.assert_called_once_with(actives, size)
        mock_stop_candles.assert_called_once_with(actives, size)