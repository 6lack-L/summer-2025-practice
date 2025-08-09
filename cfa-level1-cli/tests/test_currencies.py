import unittest
from src.cfacalc.currencies import CurrencyConverter

class TestCurrencyConverter(unittest.TestCase):

    def setUp(self):
        self.converter = CurrencyConverter()

    def test_conversion_usd_to_eur(self):
        self.converter.set_exchange_rate('USD', 'EUR', 0.85)
        result = self.converter.convert(100, 'USD', 'EUR')
        self.assertAlmostEqual(result, 85.0, places=2)

    def test_conversion_eur_to_usd(self):
        self.converter.set_exchange_rate('EUR', 'USD', 1.18)
        result = self.converter.convert(100, 'EUR', 'USD')
        self.assertAlmostEqual(result, 118.0, places=2)

    def test_invalid_currency(self):
        with self.assertRaises(ValueError):
            self.converter.convert(100, 'USD', 'XYZ')

    def test_set_exchange_rate(self):
        self.converter.set_exchange_rate('GBP', 'USD', 1.30)
        result = self.converter.convert(100, 'GBP', 'USD')
        self.assertAlmostEqual(result, 130.0, places=2)

    def test_multiple_exchange_rates(self):
        self.converter.set_exchange_rate('USD', 'JPY', 110.0)
        self.converter.set_exchange_rate('EUR', 'JPY', 130.0)
        result = self.converter.convert(100, 'USD', 'JPY')
        self.assertAlmostEqual(result, 11000.0, places=2)

if __name__ == '__main__':
    unittest.main()