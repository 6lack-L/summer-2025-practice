class BondCalculator:
    """
    A class to perform bond valuation calculations.
    """

    def __init__(self, face_value, coupon_rate, years_to_maturity, market_rate):
        self.face_value = face_value
        self.coupon_rate = coupon_rate
        self.years_to_maturity = years_to_maturity
        self.market_rate = market_rate

    def present_value_of_coupons(self):
        """
        Calculate the present value of the bond's coupon payments.
        """
        coupon_payment = self.face_value * self.coupon_rate
        pv_coupons = sum(coupon_payment / (1 + self.market_rate) ** t for t in range(1, self.years_to_maturity + 1))
        return pv_coupons

    def present_value_of_face_value(self):
        """
        Calculate the present value of the bond's face value.
        """
        return self.face_value / (1 + self.market_rate) ** self.years_to_maturity

    def bond_price(self):
        """
        Calculate the total price of the bond.
        """
        return self.present_value_of_coupons() + self.present_value_of_face_value()

    def yield_to_maturity(self, price):
        """
        Calculate the yield to maturity (YTM) of the bond.
        This is a simplified version and may require numerical methods for accurate results.
        """
        # This is a placeholder for a more complex YTM calculation
        return (self.coupon_rate * self.face_value + (self.face_value - price) / self.years_to_maturity) / \
               ((self.face_value + price) / 2)

    def current_yield(self, price):
        """
        Calculate the current yield of the bond.
        """
        return (self.face_value * self.coupon_rate) / price if price else 0

def main():
    # Example usage of the BondCalculator class
    face_value = 1000  # Example face value
    coupon_rate = 0.05  # 5% coupon rate
    years_to_maturity = 10  # 10 years to maturity
    market_rate = 0.04  # 4% market rate

    bond_calculator = BondCalculator(face_value, coupon_rate, years_to_maturity, market_rate)
    price = bond_calculator.bond_price()
    ytm = bond_calculator.yield_to_maturity(price)
    current_yield = bond_calculator.current_yield(price)

    print(f"Bond Price: {price:.2f}")
    print(f"Yield to Maturity: {ytm:.2%}")
    print(f"Current Yield: {current_yield:.2%}")

if __name__ == "__main__":
    main()