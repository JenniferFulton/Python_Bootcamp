# For this assignment, we'll add some functionality to the User class:

# make_withdrawal(self, amount) - have this method decrease the user's balance by the amount specified
# display_user_balance(self) - have this method print the user's name and account balance to the terminal
# eg. "User: Guido van Rossum, Balance: $150
# BONUS: transfer_money(self, other_user, amount) - have this method decrease the user's balance by the amount and add that amount to other other_user's balance
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
    
    def display_balance(self):
        print(self.balance)

Jen = User("Jennifer","PNC")
Merg = User("Morgan", "BOA")
Wendy = User("Wendy", "PNC")