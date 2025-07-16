import decimal

class FinanceCalculator:
    """
    A simple finance calculator for various financial calculations.
    """

    def __init__(self, principal=0, rate=0, time=0):
        self = self
        self.principal = principal
        self.rate = rate
        self.time = time

    def pva(self,compunding_frequency=0):
        """
        Calculate the present value payment of annuity.
        
        :param principal: Total amount of the loan
        :param rate: Annual interest rate (as a decimal)
        :param time: Time in years
        :return: Monthly payment amount
        """
        monthly_rate = self.rate / compunding_frequency
        number_of_payments = self.time * compunding_frequency
        return self.principal * (1 - (1/(1 + monthly_rate) ** number_of_payments))/ monthly_rate


    def calculate_future_value(self):
        """
        Calculate the future value of an investment.

        :param principal: Initial amount of money invested
        :param rate: Annual interest rate (as a decimal)
        :param time: Time in years
        :return: Future value of the investment
        """
        return self.principal * (1 + self.rate) ** self.time

    def present_value(self,future_value):
        """
        Calculate the present value of a future amount.

        :param future_value: Future amount of money
        :param rate: Annual interest rate (as a decimal)
        :param time: Time in years
        :return: Present value of the future amount
        """
        return future_value / (1 + self.rate) ** self.time

    def npv(self,cash_flows=None):
        """
        Calculate the net present value of a series of cash flows.

        :param rate: Discount rate (as a decimal)
        :param cash_flows: List of cash flows
        :return: Net present value
    """

        if cash_flows is None:
            cash_flows = []
        npv = 0
        for t, cash_flow in enumerate(cash_flows):
            npv += cash_flow / (1 + self.rate) ** t
        return npv
