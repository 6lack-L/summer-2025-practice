import unittest
from src.cfacalc.bonds import calculate_ytm, calculate_current_yield

class TestBonds(unittest.TestCase):

    def test_calculate_ytm(self):
        # Test case for yield to maturity calculation
        face_value = 1000
        coupon_rate = 0.05
        years_to_maturity = 10
        market_price = 950
        expected_ytm = 0.055  # Expected YTM value for this test case
        calculated_ytm = calculate_ytm(face_value, coupon_rate, years_to_maturity, market_price)
        self.assertAlmostEqual(calculated_ytm, expected_ytm, places=3)

    def test_calculate_current_yield(self):
        # Test case for current yield calculation
        annual_coupon_payment = 50
        market_price = 1000
        expected_current_yield = 0.05  # Expected current yield value for this test case
        calculated_current_yield = calculate_current_yield(annual_coupon_payment, market_price)
        self.assertAlmostEqual(calculated_current_yield, expected_current_yield, places=3)

if __name__ == '__main__':
    unittest.main()