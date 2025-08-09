import pytest
from cfacalc.statistics.sampling import sample_mean, sample_variance, sample_standard_deviation

def test_sample_mean():
    data = [1, 2, 3, 4, 5]
    expected_mean = 3.0
    assert sample_mean(data) == expected_mean

def test_sample_variance():
    data = [1, 2, 3, 4, 5]
    expected_variance = 2.5
    assert sample_variance(data) == expected_variance

def test_sample_standard_deviation():
    data = [1, 2, 3, 4, 5]
    expected_std_dev = 1.581
    assert round(sample_standard_deviation(data), 3) == expected_std_dev

def test_empty_data_mean():
    data = []
    expected_mean = 0.0
    assert sample_mean(data) == expected_mean

def test_empty_data_variance():
    data = []
    expected_variance = 0.0
    assert sample_variance(data) == expected_variance

def test_empty_data_standard_deviation():
    data = []
    expected_std_dev = 0.0
    assert sample_standard_deviation(data) == expected_std_dev