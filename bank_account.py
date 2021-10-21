# The BankAccount class should have a balance. When a new BankAccount instance is created, if an amount is given, the balance of the account should initially be set to that amount; otherwise, the balance should start at $0. The account should also have an interest rate, saved as a decimal (i.e. 1% would be saved as 0.01), which should be provided upon instantiation. (Hint: when using default values in parameters, the order of parameters matters!)

# The class should also have the following methods:

# deposit(self, amount) - increases the account balance by the given amount
# withdraw(self, amount) - decreases the account balance by the given amount if there are sufficient funds; if there is not enough money, print a message "Insufficient funds: Charging a $5 fee" and deduct $5
# display_account_info(self) - print to the console: eg. "Balance: $100"
# yield_interest(self) - increases the account balance by the current balance * the interest rate (as long as the balance is positive)


class BankAccount:
    def __init__(self, balance, interest_rate):
        self.balance = balance
        self.interest_rate = interest_rate
    
    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        self.balance -= amount
        return self

    def account_info(self):
        print(f"Account Balance: {self.balance}")
    
    def yield_interest(self):
        if self.balance <= 0:
            return False
        else:
            self.balance += (self.balance * (self.interest_rate/100))
            return self

# Create 2 accounts

PNC = BankAccount(2000, 3)
Discover = BankAccount(30000, 8)

# To the first account, make 3 deposits and 1 withdrawal, then calculate interest and display the account's info all in one line of code (i.e. chaining)
PNC.deposit(100).deposit(1500).deposit(300).withdraw(500).yield_interest().account_info()

# To the second account, make 2 deposits and 4 withdrawals, then calculate interest and display the account's info all in one line of code (i.e. chaining)
Discover.deposit(3000).deposit(200).withdraw(1200).withdraw(1000).withdraw(500).withdraw(2000).yield_interest().account_info()