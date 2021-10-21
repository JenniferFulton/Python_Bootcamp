# Make sure that by the end of this assignment that you:
    # have both the User and BankAccount classes in the same file for your assignment
    # only create BankAccount instances inside of the User's __init__ method
    # only call BankAccount methods inside of the methods in the User class

# Update the User class __init__ method
# Update the User class make_deposit method
# Update the User class make_withdrawal method
# Update the User class display_user_balance method
# SENSEI BONUS: Allow a user to have multiple accounts; update methods so the user has to specify which account they are withdrawing or depositing to

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

class User:
    def __init__(self, name, bank):
        self.name = name
        self.bank = bank
        self.balance = 0
    
    def make_deposits(self, amount):
        self.balance += amount
        return self
    
    def make_withdrawal(self,amount):
        self.balance -= amount
        return self
    
    def transfer_money(self, amount, who):
        self.balance -= amount
        who.balance += amount
    
    def display_balance(self):
        print(f"{self.name}'s Balance: {self.balance}")
