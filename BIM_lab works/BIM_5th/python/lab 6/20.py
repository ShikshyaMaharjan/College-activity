# Base class
class Account:
    def __init__(self, name, acc_no, acc_type, balance):
        self.customer_name = name
        self.account_number = acc_no
        self.account_type = acc_type
        self.balance = balance


# Derived class
class SavingAccount(Account):

    def deposit(self):
        amount = float(input("Enter deposit amount: "))
        self.balance += amount
        print("Amount Deposited Successfully.")

    def display_balance(self):
        print("Current Balance =", self.balance)

    def withdraw(self):
        amount = float(input("Enter withdrawal amount: "))
        if amount <= self.balance:
            self.balance -= amount
            print("Amount Withdrawn Successfully.")
        else:
            print("Insufficient Balance.")


# Main Program
name = input("Enter Customer Name: ")
acc_no = input("Enter Account Number: ")
acc_type = input("Enter Account Type: ")
balance = float(input("Enter Initial Balance: "))

obj = SavingAccount(name, acc_no, acc_type, balance)

obj.deposit()
obj.display_balance()

obj.withdraw()
obj.display_balance()