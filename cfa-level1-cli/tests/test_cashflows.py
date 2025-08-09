import pytest
from src.cfacalc.cashflows import CashFlowCalculator

def test_npv():
    calculator = CashFlowCalculator(principal=1000, rate=0.1)
    cash_flows = [200, 300, 400, 500]
    expected_npv = 200 / (1 + 0.1) + 300 / (1 + 0.1) ** 2 + 400 / (1 + 0.1) ** 3 + 500 / (1 + 0.1) ** 4 - 1000
    assert abs(calculator.npv(cash_flows) - expected_npv) < 1e-6

def test_irr():
    calculator = CashFlowCalculator(principal=1000)
    cash_flows = [-1000, 200, 300, 400, 500]
    expected_irr = 0.1  # This is a placeholder; actual IRR calculation would require a numerical method
    assert abs(calculator.irr(cash_flows) - expected_irr) < 1e-6

def test_cash_flow_analysis():
    calculator = CashFlowCalculator(principal=1000, rate=0.1)
    cash_flows = [100, 200, 300]
    npv_result = calculator.npv(cash_flows)
    irr_result = calculator.irr([-1000] + cash_flows)
    
    assert npv_result >= 0  # Assuming positive cash flows yield a non-negative NPV
    assert irr_result > 0  # Assuming cash flows yield a positive IRR

def test_invalid_cash_flows():
    calculator = CashFlowCalculator(principal=1000)
    with pytest.raises(ValueError):
        calculator.npv(None)
    with pytest.raises(ValueError):
        calculator.irr([])  # No cash flows provided should raise an error