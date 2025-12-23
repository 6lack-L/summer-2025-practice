import pytest
from src.statistics.distributions import normal_distribution, binomial_distribution

def test_normal_distribution():
    mean = 0
    std_dev = 1
    x = 1
    result = normal_distribution(x, mean, std_dev)
    expected = 0.24197072451914337  # Expected value for N(0,1) at x=1
    assert abs(result - expected) < 1e-9

def test_binomial_distribution():
    n = 10
    p = 0.5
    k = 5
    result = binomial_distribution(n, k, p)
    expected = 0.24609375000000006  # Expected value for B(10, 0.5) at k=5
    assert abs(result - expected) < 1e-9

def test_invalid_normal_distribution():
    with pytest.raises(ValueError):
        normal_distribution(1, 0, 0)  # Standard deviation cannot be zero

def test_invalid_binomial_distribution():
    with pytest.raises(ValueError):
        binomial_distribution(-1, 5, 0.5)  # n cannot be negative

def test_binomial_distribution_edge_case():
    n = 0
    p = 0.5
    k = 0
    result = binomial_distribution(n, k, p)
    expected = 1.0  # B(0, p) at k=0 should be 1
    assert result == expected