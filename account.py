def getFloat(prompt):
    while True:
        try:
            myFloat = float(input(prompt))
            return myFloat

        except ValueError:
            print('invalid entry')


def account_menu():
    # print the options you have
    print(" ")
    print("Your Transaction Options Are:")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("1) Deposit money")
    print("2) Withdraw amount")
    print("3) Check balance")
    print("4) Back")
    print(" ")
    option = int(input("Choose your option: "))
    return option


class Account:

    def __init__(self, balance, account_no):
        self.balance = float(balance)
        self.account_no = account_no

    # way of insuring you can only enter a number.

    def deposit(self, amount):
        self.balance += amount

    # this is the method for the withdraw option in the customer menu.
    def withdraw(self, amount):
        if amount > self.balance:
            print("Not enough to withdraw")
        else:
            self.balance -= amount
            print("Withdrawal is complete, the balance in your account is %.2f" % self.balance)

    def print_balance(self):
        print("Your account balance is %.2f" % self.balance)

    def get_balance(self):
        return self.balance

    def get_account_no(self):
        return self.account_no

    def run_account_options(self):
        loop = 1
        while loop == 1:
            choice = account_menu()
            if choice == 1:
                amount = getFloat("Please enter amount to be deposited: ")  ### is controlling the input.
                self.deposit(amount)
                self.print_balance()
            elif choice == 2:
                response = 'Y'
                while response.upper() == 'Y':

                    amount = getFloat("\nhow much would you like to withdraw today?: ")
                    if amount > self.get_balance():
                        print('you don\'t have enough money in your account')  ### you have to type number.
                        response = input('try again? Press Y to continue:  ')
                    else:
                        self.withdraw(amount)
                        self.print_balance()
                        break
            elif choice == 3:
                self.print_balance()
            elif choice == 4:
                loop = 0
        print("Exit account operations")

    @staticmethod
    def admin_account_menu():
        # print the options you have
        print(" ")
        print("Your Transaction Options Are:")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("1) Deposit money")
        print("2) Check balance")
        print("3) Back")
        print(" ")
        option = int(input("Choose your option: "))
        return option

    def run_admin_account_options(self):
        loop = 1
        while loop == 1:
            choice = self.admin_account_menu()
            if choice == 1:
                amount = getFloat("Please enter amount to be deposited: ")  ### is controlling the input.
                self.deposit(amount)
                self.print_balance()
            elif choice == 2:
                self.print_balance()
            elif choice == 3:
                loop = 0
        print("Exit account operations")
