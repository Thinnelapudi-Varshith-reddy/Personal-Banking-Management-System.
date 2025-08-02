import time
from time import sleep # to simulate delays in the program
class BankAccount:
    def __init__(self, name, pin, account_type="Savings", balance=0):
        self.name = name
        self.pin = pin
        self.account_type = account_type
        self.balance = balance
        self.transactions = []

    def authenticate(self, entered_pin):
        return self.pin == entered_pin

    def deposit(self, amount):
        if amount <= 0:
            print("Amount must be positive.")
            return
        self.balance += amount
        self.transactions.append(f"Deposited ₹{amount}")
        print(f"Deposited ₹{amount}. New Balance: ₹{self.balance}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Amount must be positive.")
            return
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            self.transactions.append(f"Withdrew ₹{amount}")
            print(f"Withdrew ₹{amount}. New Balance: ₹{self.balance}")

    def display(self):
        print(f"\n---- ACCOUNT DETAILS ----")
        print(f"Account Holder : {self.name}")
        print(f"Account Type   : {self.account_type}")
        print(f"Balance        : ₹{self.balance}")

    def show_transactions(self):
        print("\n---- TRANSACTION HISTORY ----")
        if not self.transactions:
            print("No transactions found.")
        else:
            for tx in self.transactions:
                print(tx)

    def calculate_interest(self, rate=3.5):
        interest = self.balance * rate / 100
        print(f"\nInterest (at {rate}%): ₹{interest:.2f}")


# Main Menu
def main():
    print("Welcome to HDFC Bank")
    name = input("Enter your name: ")
    account_type = input("Enter account type (Savings/Current): ").capitalize()
    pin = input("Set your 4-digit PIN: ")

    account = BankAccount(name, pin, account_type)

    print("\nAccount created successfully!")
    time.sleep(1)

    while True:
        print("\n==== HDFC BANK MENU ====")
        print("1. Deposit Money")
        print("2. Withdraw Money")
        print("3. Check Balance")
        print("4. Show Account Details")
        print("5. Transaction History")
        print("6. Calculate Interest")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice in ['1', '2', '3', '4', '5', '6']:
            entered_pin = input("Enter your PIN for verification: ")
            if not account.authenticate(entered_pin):
                print("Invalid PIN. Access denied.")
                continue

        if choice == '1':
            amount = float(input("Enter amount to deposit: ₹"))
            account.deposit(amount)

        elif choice == '2':
            amount = float(input("Enter amount to withdraw: ₹"))
            account.withdraw(amount)

        elif choice == '3':
            print(f"Current Balance: ₹{account.balance}")

        elif choice == '4':
            account.display()

        elif choice == '5':
            account.show_transactions()

        elif choice == '6':
            account.calculate_interest()

        elif choice == '7':
            print("Thank you for banking with HDFC! Have a great day!")
            break

        else:
            print("Invalid choice. Please select from 1 to 7.")

main()
