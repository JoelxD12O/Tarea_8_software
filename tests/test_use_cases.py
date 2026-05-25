import unittest
from unittest.mock import MagicMock
from datetime import datetime
from src.domain.entities.consumption import Consumption
from src.application.use_cases.register_consumption import RegisterConsumptionUseCase
from src.application.use_cases.process_rewards import ProcessRewardsUseCase

class TestUseCases(unittest.TestCase):
    def test_register_consumption(self):
        mock_broker = MagicMock()
        use_case = RegisterConsumptionUseCase(mock_broker)
        c = Consumption(amount=50.0, card_number="1234", restaurant_id="R1", timestamp=datetime.now())
        
        use_case.execute(c)
        mock_broker.publish_consumption.assert_called_once_with(c)

    def test_process_rewards(self):
        use_case = ProcessRewardsUseCase()
        c = Consumption(amount=100.0, card_number="1234", restaurant_id="R1", timestamp=datetime.now())
        result = use_case.execute(c)
        
        self.assertEqual(result["points"], 10)
        self.assertEqual(result["cashback"], 2.0)

if __name__ == "__main__":
    unittest.main()
