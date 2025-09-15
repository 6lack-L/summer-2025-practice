from .tvm import TimeValueOfMoney as tvm
from .cashflows import CashFlowCalculator as cfc


class CLI:
    def __init__(self):
        self.options = {
            "1": "Time Value of Money",
            "2": "Cash Flow Analysis",
            "3": "Calculate Bond Valuation",
            "4": "Calculate Equity Valuation",
            "5": "Calculate Portfolio Metrics",
            "6": "Calculate Derivative Pricing",
            "7": "Currency Conversion",
            "8": "Yield Curve Analysis",
            "": "Exit\n"
        }

    def display_menu(self):
        print("Welcome to the CFA Level 1 Financial Calculator!\n")
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
                self.tvm_sub_menu()
            elif choice == "2":
                self.cashflow_sub_menu()
            elif choice == "3":
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


    def calculate_net_present_value(self):
        # Placeholder for NPV calculation logic
        print("Net Present Value calculation not implemented yet.")

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

#?Sub menus
    def tvm_sub_menu(self):
        mydict = {
            "1": "Calculate Future Value",
            "2": "Calculate Present Value",
            "3": "Calculate Present Value of Annuity",
            " ": "Exit"
            }
        op = " "
        while op in mydict:
            if op is not None:
                print("\n--- Time Value of Money Menu ---")
                for key, value in mydict.items():
                    print(f"{key}: {value}")
                op = input(
                "\nCalculate the Time Value of Money! which function would you like to use?(Press Enter to continue(Leave blank to Exit)): "
                )
            try:
                print(f"You selected: {mydict[op]}\n")
                if mydict[op] == "Exit":
                    print("\nExiting Time Value of Money.")
                    break
                else:
                    principal = float(input("Enter the principal amount: "))
                    rate = float(input("Enter the annual interest rate (as a decimal): "))
                    time = int(input("Enter the time in years: "))
                    calc = tvm(
                        principal=principal,
                        rate=rate,
                        time=time
                        )
                    print(f"\n{mydict[op]}...\n")
                    if mydict[op] == mydict.get("1"):
                        result = calc.future_value()
                        print(f"Future Value: {result}")
                    elif mydict[op] == mydict.get("2"):
                        result = calc.present_value()
                        print(f"Present Value: {result}")
                    elif mydict[op] == mydict.get("3"):
                        c = input("Enter the number of periods(leave blank for anually): \n")
                        if c == "":
                            c = 1
                        else:
                            c = int(c)
                        result = calc.annuity_payment(compounding_frequency=c)
                        print(f"Annuity Payment: {result}")
                        result = calc.present_value_annuity(payment=calc.principal,compounding_frequency=c)
                        print(f"Present Value of Annuity: {result}")
                    print('---'*5)
            except Exception as e:
                print(f"Error: {e}")
    def cashflow_sub_menu(self):
        



        return

if __name__ == "__main__":
    cli = CLI()
    cli.run()