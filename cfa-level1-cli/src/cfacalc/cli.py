from .tvm import TimeValueOfMoney as tvm


class CLI:
    def __init__(self):
        self.options = {
            "1": "Calculate Future Value",
            "2": "Calculate Present Value",
            "3": "Calculate Net Present Value",
            "4": "Calculate Present Value of Annuity",
            "5": "Calculate Bond Valuation",
            "6": "Calculate Equity Valuation",
            "7": "Calculate Portfolio Metrics",
            "8": "Calculate Derivative Pricing",
            "9": "Currency Conversion",
            "10": "Yield Curve Analysis",
            "": "Exit"
        }

    def display_menu(self):
        print("Welcome to the CFA Level 1 Financial Calculator!")
        for key, value in self.options.items():
            print(f"{key}: {value}")

    def run(self):
        while True:
            self.display_menu()
            choice = input("Select an option: ")
            if choice == "":
                print("Exiting the calculator. Goodbye!")
                break
            self.handle_choice(choice)

    def handle_choice(self, choice):
        try:
            if choice == "1":
                self.calculate_future_value()
            elif choice == "2":
                self.calculate_present_value()
            elif choice == "3":
                self.calculate_net_present_value()
            elif choice == "4":
                self.calculate_present_value_annuity()
            elif choice == "5":
                self.calculate_bond_valuation()
            elif choice == "6":
                self.calculate_equity_valuation()
            elif choice == "7":
                self.calculate_portfolio_metrics()
            elif choice == "8":
                self.calculate_derivative_pricing()
            elif choice == "9":
                self.currency_conversion()
            elif choice == "10":
                self.yield_curve_analysis()
            else:
                print("Invalid option. Please try again.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def calculate_future_value(self):
        mydict = {
            "1": "Calculate Future Value",
            "2": "Calculate Present Value",
            "3": "Calculate Net Present Value",
            "4": "Calculate Present Value of Annuity",
            " ": "Exit"
        }
        op = " "
        while op in mydict:
            if op is not None:
                op = input(
                "\nCalculate the Time Value of Money! which function would you like to use?\n1: Calculate Future Value\n2: Calculate Present Value\n3: Calculate Net Present Value\n4: Calculate Present Value of Annuity\n :Exit\n(Press Enter to continue(Leave blank to Exit)): "
                       )
            try:
                print(f"You selected: {mydict[op]}\n")
                if mydict[op] == "Exit":
                    print("\nExiting Time Value of Money.")
                    break
                principal = float(input("Enter the principal amount: "))
                rate = float(input("Enter the annual interest rate (as a decimal): "))
                time = int(input("Enter the time in years: "))
                calc = tvm(
                    principal=principal,
                    rate=rate,
                    time=time
                    )
                result = calc.future_value()
                print(f"\n\b Future Value: {result}")
            except Exception as e:
                print(f"Error: {e}")

    def calculate_present_value(self):
        # Placeholder for present value calculation logic
        print("Present Value calculation not implemented yet.")

    def calculate_net_present_value(self):
        # Placeholder for NPV calculation logic
        print("Net Present Value calculation not implemented yet.")

    def calculate_present_value_annuity(self):
        # Placeholder for present value of annuity calculation logic
        print("Present Value of Annuity calculation not implemented yet.")

    def calculate_bond_valuation(self):
        # Placeholder for bond valuation logic
        print("Bond Valuation calculation not implemented yet.")

    def calculate_equity_valuation(self):
        # Placeholder for equity valuation logic
        print("Equity Valuation calculation not implemented yet.")

    def calculate_portfolio_metrics(self):
        # Placeholder for portfolio metrics logic
        print("Portfolio Metrics calculation not implemented yet.")

    def calculate_derivative_pricing(self):
        # Placeholder for derivative pricing logic
        print("Derivative Pricing calculation not implemented yet.")

    def currency_conversion(self):
        # Placeholder for currency conversion logic
        print("Currency Conversion not implemented yet.")

    def yield_curve_analysis(self):
        # Placeholder for yield curve analysis logic
        print("Yield Curve Analysis not implemented yet.")

if __name__ == "__main__":
    cli = CLI()
    cli.run()