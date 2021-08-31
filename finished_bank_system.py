from customer import Customer
from admin import Admin
from account import Account
from person import Person
import csv


def getRangedInt(min, max):
    while True:
        try:
            myInt = int(input('Please choose an option between %d and %d >>' % (min, max)))
            if myInt < min or myInt > max:
                print('Invalid option')
            else:
                return myInt
        except ValueError:
            print('Invalid option')


def getPosFloat(prompt):
    while True:
        try:
            myFloat = float(input(prompt))
            if myFloat < 0:
                print('Only positive numbers...')
            else:
                return myFloat
        except ValueError:
            print('Not a number invalid!')


class BankSystem(object):
    def __init__(self):
        self.customers_list = []
        self.admins_list = []
        self.load_bank_data()

    def load_bank_data(self):

        # this is how I have made a new customer database with new customers to the banking system.
        with open('customers.csv', 'r') as myFile:
            reader = csv.reader(myFile)
            for row in reader:
                tempCust = Customer(row[0], row[1], row[2:6])
                tempAccno = row[7]
                tempAccount = Account(row[6], tempAccno)
                tempCust.open_account(tempAccount)

                self.customers_list.append(tempCust)
            print('%d records read' % len(self.customers_list))

        with open('Admins.csv', 'r') as myFile2:
            reader = csv.reader(myFile2)
            for row in reader:
                tempAdmin = Admin(row[0], row[1], bool(row[2]), row[3:7])
                self.admins_list.append(tempAdmin)

    def customer_login(self, name, password):
        # Step A.1
        found_customer = self.search_customers_by_name(name)

        if found_customer is not None:
            if found_customer.check_password(password):
                self.run_customer_options(found_customer)
            else:
                print("Wrong Username or Password")
                print(" You have 3 attempts left to input the correct password")
                # you have 3 attempts to type in the correct password if you don't do this you will be returned to the main menu with this function.
                tries = [2, 1, 0]
                for t in tries:
                    re_password = input('\nPlease re enter your Password: ')
                    if not found_customer.check_password(re_password):
                        print('Wrong Username or Password')
                        print('%d attempt(s) left' % t)
                    else:
                        self.run_customer_options(found_customer)
                        break

        elif found_customer is None:
            print('Wrong Username or Password')
            new_name = input('\nPlease re enter your Name: ')
            found_customer = self.search_customers_by_name(new_name)

            tries = [2, 1, 0]
            for s in tries:
                if found_customer is not None:
                    password = input('\nPlease re enter your Password: ')
                    if found_customer.check_password(password):
                        self.run_customer_options(found_customer)
                    else:
                        print('Wrong Username or Password')
                        print('%d Sorry no more attempt(s)' % s)

    def search_customers_by_name(self, customer_name):
        # STEP A.2
        found_customer = None
        for a in self.customers_list:
            name = a.get_name()
            if name.lower() == customer_name.lower():
                found_customer = a
                break
        if found_customer is None:
            print("\nThe customer %s does not exist! Please try again....|n" % customer_name)
        return found_customer

    @staticmethod
    def main_menu():
        # print the options you have
        print()
        print()
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("Welcome to the Python Bank System")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("1) Admin login")
        print("2) Customer login")
        print("3) Quit Python Bank System")
        print(" ")
        option = getRangedInt(1, 3)
        return option

    def saveBankData(self):
        with open('cust.csv', 'w', newline='') as myFile:
            writer = csv.writer(myFile, delimiter=',')
            for c in self.customers_list:
                rec = c.get_name() + ',' + c.get_password() + ',' + (c.get_address())[0] + ',' + (c.get_address())[
                    2] + ',' + (c.get_address())[3] + ',' + str((c.get_account()).get_balance())
                row = rec.split(',')
                writer.writerow(row)

    def run_main_option(self):
        loop = 1
        while loop == 1:
            choice = self.main_menu()
            if choice == 1:
                name = input("\nPlease input an admin name: ")
                password = input("\nPlease input an admin password: ")
                self.admin_login(name, password)
                print("msg")
            elif choice == 2:
                name = input("\nPlease input a customer name: ")
                password = input("\nPlease input a customer password: ")
                self.customer_login(name, password)
                print("msg")
            elif choice == 3:
                self.saveBankData()
                print('Records saved')
                loop = 0
        print("Thank-You for stopping by the bank! Your custom is appreciated")

    @staticmethod
    def customer_menu(customer_name):
        # print the options you have
        print(" ")
        print("Welcome %s : Your transaction options are:" % customer_name)
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("1) Transfer Money")
        print("2) Other Account Operations")
        print("3) Profile Settings")
        print("4) Sign Out")
        print(" ")
        option = getRangedInt(1, 4)
        return option

    def run_customer_options(self, customer):

        account = customer.get_account()
        loop = 1
        while loop == 1:
            # transferring money method.
            choice = self.customer_menu(customer.get_name())
            if choice == 1:
                customer_name = input('Please enter recipients\'s name >> ')
                trans_amount = float(input('How much do you want to transfer? >> '))
                toCustomer = self.search_customers_by_name(customer_name)
                transferToAccount = toCustomer.get_account()
                transferToAccount.deposit(trans_amount)
                account.withdraw(trans_amount)
                print("Transfer Complete")
                print("Your New balance is {}".format(account.get_balance()))
            elif choice == 2:
                account.run_account_options()
            elif choice == 3:
                customer.run_profile_options()
            elif choice == 4:
                loop = 0
        print("Exit account operations")

    def admin_login(self, name, password):
        # STEP A.3
        found_admin = self.search_admin_by_name(name)

        if found_admin is not None:
            if found_admin.check_password(password):
                self.run_admin_options(found_admin)
            else:
                print("Wrong Username or Password")
                print("3 attempts left")
                # My method of password validation.
                tries = [2, 1, 0]
                for t in tries:
                    re_password = input('\nPlease re_enter Password: ')
                    if found_admin.check_password(re_password):
                        self.run_admin_options(found_admin)
                        break
                    else:
                        print('Wrong Username or Password')
                        print('%d attempt(s) left' % t)

        elif found_admin is None:
            print('Wrong Username or Password')
            new_admin = input('\nPlease re enter your admin_name : ')
            found_admin = self.search_admin_by_name(new_admin)

            tries = [2, 1, 0]
            for s in tries:
                if found_admin is not None:
                    re_password = input('\nPlease re_enter your Password: ')
                    if found_admin.check_password(re_password):
                        self.run_admin_options(found_admin)
                    else:
                        print('Wrong Username or Password')
                        print('%d more attempt(s)' % s)

    def search_admin_by_name(self, admin_name):
        # STEP A.4
        found_admin = None
        for a in self.admins_list:
            name = a.get_name()
            if name.upper() == admin_name.upper():
                found_admin = a
                break
        if found_admin is None:
            print("\nThe customer %s does not exist! try again....|n" % admin_name)
        return found_admin

    @staticmethod
    def admin_menu(admin_name):
        # print the options you have
        print(" ")
        print("Welcome Admin %s : Available options are:" % admin_name)
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("1) Customer account operations")
        print("2) Customer profile settings")
        print("3) Admin profile settings")
        print("4) Delete customer")
        print("5) Print all customers detail")
        print("6) Sign out")
        print(" ")
        option = getRangedInt(1, 6)
        return option

    def run_admin_options(self, admin):

        loop = 1
        while loop == 1:
            choice = self.admin_menu(admin.get_name())
            if choice == 1:
                customer_name = input("\nPlease input a customers name : ")
                customer = self.search_customers_by_name(customer_name)
                if customer is not None:
                    account = customer.get_account()
                if account is not None:
                    account.run_admin_account_options()

                # pass
            elif choice == 2:
                # STEP A.5
                customer_name = input("\nPlease input a customer name : ")
                customer = self.search_customers_by_name(customer_name)

                # if customer != None:
                # account = customer.get_account()

                if customer is not None:
                    Person.run_profile_options(customer)


            elif choice == 3:
                # STEP A.6
                admin_name = input("\nplease input an admin name : ")
                admin = self.search_admin_by_name(admin_name)
                if admin is not None:
                    Person.run_profile_options(admin)

            elif choice == 4:

                # STEP A.8
                if admin.has_full_admin_right():
                    customer_name = input("\nplease input the customers name you want to delete :\n")
                    customer_account = self.search_customers_by_name(customer_name)
                    if customer_account is not None:
                        self.customers_list.remove(customer_account)
                else:
                    print("\nOnly administrators with full admin rights can remove a customer from the bank system!\n")
            elif choice == 5:
                # STEP A.9
                self.print_all_accounts_details()
            elif choice == 6:
                loop = 0
        print("Exit account operations")

    def print_all_accounts_details(self):
        # list related operation - move to main.py
        i = 0
        for c in self.customers_list:
            i += 1
            print('\n %d. ' % i, end=' ')
            c.print_details()
            print("------------------------")


app = BankSystem()
app.run_main_option()
