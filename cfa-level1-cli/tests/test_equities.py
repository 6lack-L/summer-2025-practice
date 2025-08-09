import unittest
from src.cfacalc.equities import dividend_discount_model, price_to_earnings_ratio

class TestEquities(unittest.TestCase):

    def test_dividend_discount_model(self):
        # Test for the dividend discount model calculation
        expected_value = 100.0  # Example expected value
        dividend = 5.0
        growth_rate = 0.05
        discount_rate = 0.10
        result = dividend_discount_model(dividend, growth_rate, discount_rate)
        self.assertAlmostEqual(result, expected_value, places=2)

    def test_price_to_earnings_ratio(self):
        # Test for the price to earnings ratio calculation
        expected_ratio = 20.0  # Example expected ratio
        price = 100.0
        earnings_per_share = 5.0
        result = price_to_earnings_ratio(price, earnings_per_share)
        self.assertAlmostEqual(result, expected_ratio, places=2)

if __name__ == '__main__':
    unittest.main()