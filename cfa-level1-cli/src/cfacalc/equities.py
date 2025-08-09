class EquityValuation:
    """
    A class to perform equity valuation calculations.
    """

    @staticmethod
    def dividend_discount_model(dividend, growth_rate, discount_rate):
        """
        Calculate the intrinsic value of a stock using the Dividend Discount Model (DDM).

        :param dividend: Expected annual dividend payment
        :param growth_rate: Expected growth rate of dividends (as a decimal)
        :param discount_rate: Required rate of return (as a decimal)
        :return: Intrinsic value of the stock
        """
        if discount_rate <= growth_rate:
            raise ValueError("Discount rate must be greater than growth rate.")
        return dividend / (discount_rate - growth_rate)

    @staticmethod
    def price_to_earnings_ratio(price, earnings_per_share):
        """
        Calculate the Price-to-Earnings (P/E) ratio.

        :param price: Current market price of the stock
        :param earnings_per_share: Earnings per share (EPS)
        :return: P/E ratio
        """
        if earnings_per_share <= 0:
            raise ValueError("Earnings per share must be greater than zero.")
        return price / earnings_per_share

    @staticmethod
    def earnings_growth_rate(previous_earnings, current_earnings):
        """
        Calculate the earnings growth rate.

        :param previous_earnings: Earnings from the previous period
        :param current_earnings: Earnings from the current period
        :return: Growth rate (as a decimal)
        """
        if previous_earnings <= 0:
            raise ValueError("Previous earnings must be greater than zero.")
        return (current_earnings - previous_earnings) / previous_earnings

    @staticmethod
    def required_rate_of_return(risk_free_rate, beta, market_return):
        """
        Calculate the required rate of return using the Capital Asset Pricing Model (CAPM).

        :param risk_free_rate: Risk-free rate of return (as a decimal)
        :param beta: Beta of the stock
        :param market_return: Expected market return (as a decimal)
        :return: Required rate of return (as a decimal)
        """
        return risk_free_rate + beta * (market_return - risk_free_rate)