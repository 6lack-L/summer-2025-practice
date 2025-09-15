class TimeValueOfMoney:
    def __init__(self, principal, rate, time):
        self.principal = principal
        self.rate = rate
        self.time = time

    def future_value(self):
        return self.principal * (1 + self.rate) ** self.time

    def present_value(self):
        return self.principal / (1 + self.rate) ** self.time

    def annuity_payment(self, compounding_frequency=1):
        monthly_rate = self.rate / compounding_frequency
        number_of_payments = self.time * compounding_frequency
        return self.principal * (monthly_rate / (1 - (1 + monthly_rate) ** -number_of_payments))

    def present_value_annuity(self, payment=0.0, compounding_frequency=1):
        monthly_rate = self.rate / compounding_frequency
        number_of_payments = self.time * compounding_frequency
        return payment * ((1 - (1 + monthly_rate) ** -number_of_payments) / monthly_rate)