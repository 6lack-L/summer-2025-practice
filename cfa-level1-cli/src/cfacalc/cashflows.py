class CashFlowCalculator:
    """
    A class to handle cash flow analysis calculations.
    """

    @staticmethod
    def npv(rate, cash_flows):
        """
        Calculate the net present value (NPV) of a series of cash flows.

        :param rate: Discount rate (as a decimal)
        :param cash_flows: List of cash flows
        :return: Net present value
        """
        npv = 0
        for t, cash_flow in enumerate(cash_flows):
            npv += cash_flow / (1 + rate) ** t
        return npv

    @staticmethod
    def irr(cash_flows):
        """
        Calculate the internal rate of return (IRR) for a series of cash flows.

        :param cash_flows: List of cash flows
        :return: Internal rate of return
        """
        from scipy.optimize import newton

        def npv_func(rate):
            return CashFlowCalculator.npv(rate, cash_flows)

        return newton(npv_func, 0.1)  # Initial guess of 10% for IRR

    @staticmethod
    def payback_period(cash_flows):
        """
        Calculate the payback period for a series of cash flows.

        :param cash_flows: List of cash flows
        :return: Payback period in years
        """
        cumulative_cash_flow = 0
        for t, cash_flow in enumerate(cash_flows):
            cumulative_cash_flow += cash_flow
            if cumulative_cash_flow >= 0:
                return t
        return None  # Payback period not reached

    @staticmethod
    def discounted_payback_period(rate, cash_flows):
        """
        Calculate the discounted payback period for a series of cash flows.

        :param rate: Discount rate (as a decimal)
        :param cash_flows: List of cash flows
        :return: Discounted payback period in years
        """
        cumulative_cash_flow = 0
        for t, cash_flow in enumerate(cash_flows):
            discounted_cash_flow = cash_flow / (1 + rate) ** t
            cumulative_cash_flow += discounted_cash_flow
            if cumulative_cash_flow >= 0:
                return t
        return None  # Discounted payback period not reached