# BankAccount represents a simple bank account with an account number and balance.
class BankAccount:
    def __init__(self, account_number, balance):
        # Store the account details privately using a single underscore for encapsulation.
        self._account_number = account_number
        self._balance = balance

    def set_account_number(self, account_number):
        # Update the account number when needed.
        self._account_number = account_number

    def set_balance(self, balance):
        # Only allow non-negative balances; ignore invalid negative values.
        if balance >= 0:
            self._balance = balance
            return self._balance
        else:
            print("The balance must be not be a negative number.")
            return None

    def get_account_number(self):
        # Return the account number.
        return self._account_number

    def get_balance(self):
        # Return the current balance.
        return self._balance

allaccounts = []
a1 = BankAccount(12345, 1000)
allaccounts.append(a1)

print(f"Account {len(allaccounts)}")
print(f"Account Number: {allaccounts[0].get_account_number()}")
print(f"Balance: {allaccounts[0].get_balance():.2f}")

a1.set_balance(-100)
print(f"Account Number: {allaccounts[0].get_account_number()}")
print(f"Balance: {allaccounts[0].get_balance():.2f}")
