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

class User:
    def __init__(self, name, account):
        self.name = name
        self.account = BankAccount(1000,3)
    
    def make_deposits(self, amount):
        self.account.balance += amount
        return self
    
    def make_withdrawal(self,amount):
        self.account.balance -= amount
        return self
    
    def transfer_money(self, amount, who):
        self.account.balance -= amount
        who.account.balance += amount
        return self

    def yield_interest(self):
        if self.account.balance <= 0:
            return False
        else:
            self.account.balance += (self.account.balance * (self.account.interest_rate/100))
            return self
    
    def display_balance(self):
        print(f"{self.name}'s Balance: {self.account.balance}")

PNC = BankAccount(1000,5)
Jen = User("Jennifer",PNC)

BOA = BankAccount(100,3)
Merg = User("Merg", BOA)



Jen.make_deposits(100).make_deposits(100).make_withdrawal(50).yield_interest().transfer_money(184.5, Merg).display_balance()
Merg.display_balance()


