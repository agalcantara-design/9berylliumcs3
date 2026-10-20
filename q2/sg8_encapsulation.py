class BankAccount: # defines a class called BankAccount
    def __init__(self, account_number, balance): # initializes the class with account_number and balance
        self._account_number = account_number # stores the account number privately
        self._balance = balance #  stores the balance privately

    def set_account_number(self, account_number): # defines a method to set the account number
        self._account_number = account_number 

    def set_balance(self, balance): # defines a method for setting balance
        if balance >= 0: # checks if the balance is greater than or equal to 0
            self._balance = balance
            return self._balance
        else:
            print("The balance must be not be a negative number.") # error message
            return None

    def get_account_number(self): # defines a method for getting the account number
        return self._account_number

    def get_balance(self): # defines a method for getting the balance
        return self._balance

allaccounts = [] # empty list called allaccounts
a1 = BankAccount(12345, 1000) # object BankAccount with account number 12345 and balance of 1000
allaccounts.append(a1)  # appends a1 to the allacounts list

print(f"Account {len(allaccounts)}") # prints and displays Account
print(f"Account Number: {allaccounts[0].get_account_number()}") # displays the account number
print(f"Balance: {allaccounts[0].get_balance():.2f}") # displays the balance

a1.set_balance(-100) # sets the balance to an invalid value
print(f"Account Number: {allaccounts[0].get_account_number()}") #  displays the account number
print(f"Balance: {allaccounts[0].get_balance():.2f}") # displays the balance
