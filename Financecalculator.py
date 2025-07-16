import fractions
import math
import decimal

class FinanceCalculator:
    """
    A simple finance calculator for various financial calculations.
    """

    def __init__(self, principal=0, rate=0, time=0):
        self.principal = principal
        self.rate = rate
        self.time = time

    def calculate_loan_payment(self):
        """
        Calculate the monthly payment for a loan.
        
        :param principal: Total amount of the loan
        :param rate: Annual interest rate (as a decimal)
        :param time: Time in years
        :return: Monthly payment amount
        """
        monthly_rate = rate / 12
        number_of_payments = time * 12
        return principal * (monthly_rate * (1 + monthly_rate) ** number_of_payments) / ((1 + monthly_rate) ** number_of_payments - 1)


    def calculate_future_value(principal, rate, time):
        """
        Calculate the future value of an investment.

        :param principal: Initial amount of money invested
        :param rate: Annual interest rate (as a decimal)
        :param time: Time in years
        :return: Future value of the investment
        """
        return principal * (1 + rate) ** time

    def present_value(future_value, rate, time):
        """
        Calculate the present value of a future amount.

        :param future_value: Future amount of money
        :param rate: Annual interest rate (as a decimal)
        :param time: Time in years
        :return: Present value of the future amount
        """
        return future_value / (1 + rate) ** time

    def npv(rate=0, cash_flows=):
        """
        Calculate the net present value of a series of cash flows.

        :param rate: Discount rate (as a decimal)
        :param cash_flows: List of cash flows
        :return: Net present value
    """
        return