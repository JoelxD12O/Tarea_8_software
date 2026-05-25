import unittest
from datetime import datetime
from src.domain.entities.consumption import Consumption

class TestConsumption(unittest.TestCase):
    def test_calculate_points(self):
        c = Consumption(amount=105.0, card_number="1234", restaurant_id="R1", timestamp=datetime.now())
        self.assertEqual(c.calculate_points(), 10)

    def test_calculate_cashback(self):
        c = Consumption(amount=100.0, card_number="1234", restaurant_id="R1", timestamp=datetime.now())
        self.assertEqual(c.calculate_cashback(), 2.0)

if __name__ == "__main__":
    unittest.main()
