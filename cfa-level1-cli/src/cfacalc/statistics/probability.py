from scipy.stats import norm

def normal_distribution(x, mean=0, std_dev=1):
    """
    Calculate the probability density function for a normal distribution.

    :param x: Value for which to calculate the PDF
    :param mean: Mean of the distribution
    :param std_dev: Standard deviation of the distribution
    :return: Probability density function value
    """
    return norm.pdf(x, mean, std_dev)

def cumulative_normal_distribution(x, mean=0, std_dev=1):
    """
    Calculate the cumulative distribution function for a normal distribution.

    :param x: Value for which to calculate the CDF
    :param mean: Mean of the distribution
    :param std_dev: Standard deviation of the distribution
    :return: Cumulative distribution function value
    """
    return norm.cdf(x, mean, std_dev)

def binomial_probability(n, k, p):
    """
    Calculate the probability of k successes in n trials for a binomial distribution.

    :param n: Number of trials
    :param k: Number of successes
    :param p: Probability of success on an individual trial
    :return: Probability of k successes
    """
    from math import comb
    return comb(n, k) * (p ** k) * ((1 - p) ** (n - k))

def expected_value(probabilities, values):
    """
    Calculate the expected value of a random variable.

    :param probabilities: List of probabilities
    :param values: List of corresponding values
    :return: Expected value
    """
    return sum(p * v for p, v in zip(probabilities, values))

def variance(probabilities, values):
    """
    Calculate the variance of a random variable.

    :param probabilities: List of probabilities
    :param values: List of corresponding values
    :return: Variance
    """
    mean = expected_value(probabilities, values)
    return sum(p * (v - mean) ** 2 for p, v in zip(probabilities, values))