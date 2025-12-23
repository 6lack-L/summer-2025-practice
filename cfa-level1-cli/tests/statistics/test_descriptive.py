import pytest
from  import mean, median, standard_deviation

def test_mean():
    data = [1, 2, 3, 4, 5]
    assert mean(data) == 3.0

def test_median():
    data_odd = [1, 2, 3, 4, 5]
    data_even = [1, 2, 3, 4]
    assert median(data_odd) == 3.0
    assert median(data_even) == 2.5

def test_standard_deviation():
    data = [1, 2, 3, 4, 5]
    assert round(standard_deviation(data), 2) == 1.58