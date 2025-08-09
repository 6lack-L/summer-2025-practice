import unittest
from src.cfacalc.derivatives import calculate_option_price, calculate_futures_price

class TestDerivatives(unittest.TestCase):

    def test_calculate_option_price(self):
        # Test parameters for option pricing
        S = 100  # Current stock price
        K = 100  # Strike price
        T = 1    # Time to expiration in years
        r = 0.05 # Risk-free interest rate
        sigma = 0.2 # Volatility

        # Call option price
        call_price = calculate_option_price(S, K, T, r, sigma, option_type='call')
        self.assertGreater(call_price, 0)

        # Put option price
        put_price = calculate_option_price(S, K, T, r, sigma, option_type='put')
        self.assertGreater(put_price, 0)

    def test_calculate_futures_price(self):
        # Test parameters for futures pricing
        S = 100  # Current spot price
        r = 0.05 # Risk-free interest rate
        T = 1    # Time to expiration in years

        futures_price = calculate_futures_price(S, r, T)
        self.assertEqual(futures_price, S * (1 + r)**T)

if __name__ == '__main__':
    unittest.main()