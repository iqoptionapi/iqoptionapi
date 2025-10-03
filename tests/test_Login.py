import unittest
from unittest.mock import patch, MagicMock
from iqoptionapi.stable_api import IQ_Option
import iqoptionapi.global_value as global_value

class TestLogin(unittest.TestCase):

    @patch('iqoptionapi.stable_api.IQOptionAPI')
    def test_login(self, mock_iq_option_api):
        # Arrange
        mock_api_instance = MagicMock()
        mock_api_instance.connect.return_value = (True, None)

        mock_api_instance.profile.msg = {
            "balances": [
                {"id": 4, "type": 4, "amount": 10000}
            ]
        }

        def mock_reset_training_balance():
            mock_api_instance.training_balance_reset_request = {"isSuccessful": True, "msg": "Balance reset"}

        mock_api_instance.reset_training_balance.side_effect = mock_reset_training_balance

        mock_iq_option_api.return_value = mock_api_instance

        global_value.balance_id = 4
        global_value.check_websocket_if_connect = True

        try:
            # Act
            iq_option = IQ_Option("test@email.com", "password")
            connect_status, connect_reason = iq_option.connect()

            iq_option.change_balance("PRACTICE")
            reset_result = iq_option.reset_practice_balance()
            check_connect_result = iq_option.check_connect()

            # Assert
            self.assertTrue(connect_status)
            self.assertIsNone(connect_reason)
            self.assertTrue(check_connect_result)
            self.assertTrue(reset_result["isSuccessful"])

            mock_api_instance.connect.assert_called_once()
            mock_api_instance.reset_training_balance.assert_called_once()

        finally:
            # Teardown: Reset global values
            global_value.balance_id = None
            global_value.check_websocket_if_connect = None