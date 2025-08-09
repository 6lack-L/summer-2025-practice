class YieldCurveCalculator:
    """
    A class to handle yield curve calculations and analysis.
    """

    def __init__(self):
        pass

    def calculate_spot_rates(self, cash_flows, maturities):
        """
        Calculate spot rates from cash flows and maturities.

        :param cash_flows: List of cash flows
        :param maturities: List of maturities corresponding to cash flows
        :return: List of calculated spot rates
        """
        spot_rates = []
        for i in range(len(cash_flows)):
            spot_rate = (cash_flows[i] / (1 + spot_rates[i-1]) ** maturities[i]) - 1 if i > 0 else cash_flows[i] / maturities[i]
            spot_rates.append(spot_rate)
        return spot_rates

    def calculate_forward_rates(self, spot_rates):
        """
        Calculate forward rates from spot rates.

        :param spot_rates: List of spot rates
        :return: List of calculated forward rates
        """
        forward_rates = []
        for i in range(1, len(spot_rates)):
            forward_rate = ((1 + spot_rates[i]) ** (i + 1) / (1 + spot_rates[i - 1]) ** i) - 1
            forward_rates.append(forward_rate)
        return forward_rates

    def plot_yield_curve(self, maturities, rates):
        """
        Plot the yield curve based on maturities and rates.

        :param maturities: List of maturities
        :param rates: List of rates (spot or forward)
        """
        import matplotlib.pyplot as plt

        plt.figure(figsize=(10, 6))
        plt.plot(maturities, rates, marker='o')
        plt.title('Yield Curve')
        plt.xlabel('Maturity (Years)')
        plt.ylabel('Yield (%)')
        plt.grid()
        plt.show()