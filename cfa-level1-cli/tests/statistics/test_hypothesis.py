import pytest
from cfacalc.statistics.hypothesis import t_test, z_test, chi_square_test

def test_t_test():
    sample_data = [2.3, 2.5, 2.7, 2.9, 3.0]
    population_mean = 2.5
    alpha = 0.05
    result = t_test(sample_data, population_mean, alpha)
    assert result['reject_null'] is True  # Adjust based on expected outcome

def test_z_test():
    sample_mean = 100
    population_mean = 95
    population_std = 10
    sample_size = 30
    alpha = 0.05
    result = z_test(sample_mean, population_mean, population_std, sample_size, alpha)
    assert result['reject_null'] is False  # Adjust based on expected outcome

def test_chi_square_test():
    observed = [10, 20, 30]
    expected = [15, 15, 30]
    alpha = 0.05
    result = chi_square_test(observed, expected, alpha)
    assert result['reject_null'] is True  # Adjust based on expected outcome