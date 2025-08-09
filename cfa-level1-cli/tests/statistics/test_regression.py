import pytest
from cfacalc.statistics.regression import linear_regression, multiple_regression

def test_linear_regression():
    x = [1, 2, 3, 4, 5]
    y = [2, 3, 5, 7, 11]
    slope, intercept = linear_regression(x, y)
    assert round(slope, 2) == 1.8
    assert round(intercept, 2) == 0.4

def test_multiple_regression():
    import numpy as np
    x = np.array([[1, 1], [1, 2], [2, 2], [2, 3]])
    y = np.array([1, 2, 2, 3])
    coefficients = multiple_regression(x, y)
    assert len(coefficients) == 2
    assert round(coefficients[0], 2) == 0.5
    assert round(coefficients[1], 2) == 0.5