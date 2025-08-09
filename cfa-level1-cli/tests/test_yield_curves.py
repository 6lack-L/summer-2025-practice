import pytest
from src.cfacalc.yield_curves import YieldCurve

def test_yield_curve_creation():
    curve = YieldCurve([0.01, 0.02, 0.03], [1, 2, 3])
    assert curve.rates == [0.01, 0.02, 0.03]
    assert curve.maturities == [1, 2, 3]

def test_yield_curve_forward_rate():
    curve = YieldCurve([0.01, 0.02, 0.03], [1, 2, 3])
    forward_rate = curve.forward_rate(1, 2)
    assert round(forward_rate, 4) == 0.0300

def test_yield_curve_discount_factor():
    curve = YieldCurve([0.01, 0.02, 0.03], [1, 2, 3])
    discount_factor = curve.discount_factor(2)
    assert round(discount_factor, 4) == 0.9804

def test_yield_curve_zero_coupon_bond_price():
    curve = YieldCurve([0.01, 0.02, 0.03], [1, 2, 3])
    price = curve.zero_coupon_bond_price(3, 1000)
    assert round(price, 2) == 905.73

def test_yield_curve_pars():
    curve = YieldCurve([0.01, 0.02, 0.03], [1, 2, 3])
    par_value = curve.par_value(1000)
    assert round(par_value, 2) == 1000.00

def test_yield_curve_invalid_maturities():
    with pytest.raises(ValueError):
        YieldCurve([0.01, 0.02], [1, 2, 3])  # Mismatched lengths

def test_yield_curve_invalid_rates():
    with pytest.raises(ValueError):
        YieldCurve([0.01, -0.02, 0.03], [1, 2, 3])  # Negative rate

def test_yield_curve_invalid_maturity_value():
    curve = YieldCurve([0.01, 0.02, 0.03], [1, 2, 3])
    with pytest.raises(ValueError):
        curve.discount_factor(5)  # Maturity not in curve