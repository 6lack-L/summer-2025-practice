class DerivativesCalculator:
    """
    A class to handle calculations related to derivatives, including options pricing and futures contracts.
    """

    def __init__(self):
        pass

    def black_scholes(self, S, K, T, r, sigma, option_type='call'):
        """
        Calculate the Black-Scholes option pricing.

        :param S: Current stock price
        :param K: Option strike price
        :param T: Time to expiration in years
        :param r: Risk-free interest rate (as a decimal)
        :param sigma: Volatility of the stock (as a decimal)
        :param option_type: 'call' for call option, 'put' for put option
        :return: Price of the option
        """
        from math import log, sqrt, exp
        from scipy.stats import norm

        d1 = (log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * sqrt(T))
        d2 = d1 - sigma * sqrt(T)

        if option_type == 'call':
            option_price = (S * norm.cdf(d1) - K * exp(-r * T) * norm.cdf(d2))
        elif option_type == 'put':
            option_price = (K * exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1))
        else:
            raise ValueError("Invalid option type. Use 'call' or 'put'.")

        return option_price

    def futures_price(self, S, r, T):
        """
        Calculate the futures price.

        :param S: Current spot price
        :param r: Risk-free interest rate (as a decimal)
        :param T: Time to expiration in years
        :return: Futures price
        """
        return S * exp(r * T)

    def option_greeks(self, S, K, T, r, sigma, option_type='call'):
        """
        Calculate the Greeks for options.

        :param S: Current stock price
        :param K: Option strike price
        :param T: Time to expiration in years
        :param r: Risk-free interest rate (as a decimal)
        :param sigma: Volatility of the stock (as a decimal)
        :param option_type: 'call' for call option, 'put' for put option
        :return: Dictionary containing Delta, Gamma, Vega, Theta, and Rho
        """
        from math import log, sqrt, exp
        from scipy.stats import norm

        d1 = (log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * sqrt(T))
        d2 = d1 - sigma * sqrt(T)

        delta = norm.cdf(d1) if option_type == 'call' else norm.cdf(d1) - 1
        gamma = norm.pdf(d1) / (S * sigma * sqrt(T))
        vega = S * norm.pdf(d1) * sqrt(T)
        theta = (-S * norm.pdf(d1) * sigma / (2 * sqrt(T)) - r * K * exp(-r * T) * norm.cdf(d2)) if option_type == 'call' else (-S * norm.pdf(d1) * sigma / (2 * sqrt(T)) + r * K * exp(-r * T) * norm.cdf(-d2))
        rho = K * T * exp(-r * T) * norm.cdf(d2) if option_type == 'call' else -K * T * exp(-r * T) * norm.cdf(-d2)

        return {
            'Delta': delta,
            'Gamma': gamma,
            'Vega': vega,
            'Theta': theta,
            'Rho': rho
        }