import pytest
from cfacalc.statistics.probability import calculate_probability, binomial_probability

def test_calculate_probability():
    assert calculate_probability(0.5, 10) == 0.5  # Example test case
    assert calculate_probability(0.2, 5) == 0.2  # Example test case

def test_binomial_probability():
    assert binomial_probability(5, 10, 0.5) == 0.24609375  # Example test case
    assert binomial_probability(3, 10, 0.3) == 0.215233  # Example test case

# Add more tests as needed for comprehensive coverage