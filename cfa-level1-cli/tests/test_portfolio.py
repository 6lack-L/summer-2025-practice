import unittest
from src.cfacalc.portfolio import Portfolio

class TestPortfolio(unittest.TestCase):

    def setUp(self):
        self.portfolio = Portfolio()

    def test_add_asset(self):
        self.portfolio.add_asset('AAPL', 10, 150)
        self.assertIn('AAPL', self.portfolio.assets)
        self.assertEqual(self.portfolio.assets['AAPL']['quantity'], 10)
        self.assertEqual(self.portfolio.assets['AAPL']['price'], 150)

    def test_remove_asset(self):
        self.portfolio.add_asset('AAPL', 10, 150)
        self.portfolio.remove_asset('AAPL')
        self.assertNotIn('AAPL', self.portfolio.assets)

    def test_calculate_total_value(self):
        self.portfolio.add_asset('AAPL', 10, 150)
        self.portfolio.add_asset('GOOGL', 5, 1000)
        total_value = self.portfolio.calculate_total_value()
        self.assertEqual(total_value, 1500 + 5000)

    def test_asset_allocation(self):
        self.portfolio.add_asset('AAPL', 10, 150)
        self.portfolio.add_asset('GOOGL', 5, 1000)
        allocation = self.portfolio.asset_allocation()
        self.assertEqual(allocation['AAPL'], 0.23, places=2)
        self.assertEqual(allocation['GOOGL'], 0.77, places=2)

if __name__ == '__main__':
    unittest.main()