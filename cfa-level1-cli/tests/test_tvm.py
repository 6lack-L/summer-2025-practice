import unittest
from src.cfacalc.tvm import FinanceCalculator

class TestTimeValueOfMoney(unittest.TestCase):

    def setUp(self):
        self.calculator = FinanceCalculator(principal=1000, rate=0.05, time=5)

    def test_future_value(self):
        expected_future_value = 1000 * (1 + 0.05) ** 5
        self.assertAlmostEqual(self.calculator.calculate_future_value(), expected_future_value, places=2)

    def test_present_value(self):
        future_value = 1276.28  # Future value after 5 years at 5%
        expected_present_value = future_value / (1 + 0.05) ** 5
        self.assertAlmostEqual(self.calculator.present_value(future_value), expected_present_value, places=2)

    def test_present_value_annuity(self):
        compounding_frequency = 12  # Monthly
        expected_pva = 1000 * (1 - (1 / (1 + (0.05 / compounding_frequency)) ** (5 * compounding_frequency))) / (0.05 / compounding_frequency)
        self.assertAlmostEqual(self.calculator.pva(compounding_frequency), expected_pva, places=2)

    def test_npv(self):
        cash_flows = [200, 300, 400, 500, 600]
        expected_npv = sum(cf / (1 + 0.05) ** i for i, cf in enumerate(cash_flows)) - self.calculator.principal
        self.assertAlmostEqual(self.calculator.npv(cash_flows), expected_npv, places=2)

if __name__ == '__main__':
    unittest.main()