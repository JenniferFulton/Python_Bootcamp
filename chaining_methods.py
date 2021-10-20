#For previous user.py file, update it so that each instance's methods are chained

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
    
    def transfer_money(self, amount, who):
        self.balance -= amount
        who.balance += amount
        return self
    
    def display_balance(self):
        print(f"{self.name}'s Balance: {self.balance}")


Jen = User("Jennifer","PNC")
Merg = User("Morgan", "BOA")
Wendy = User("Wendy", "PNC")

# Have the first user make 3 deposits and 1 withdrawal and then display their balance
Jen.make_deposits(100).make_deposits(50).make_deposits(200).make_withdrawal(25).display_balance()

# Have the second user make 2 deposits and 2 withdrawals and then display their balance
Merg.make_deposits(500).make_deposits(20).make_withdrawal(57).display_balance()

# Have the third user make 1 deposits and 3 withdrawals and then display their balance
Wendy.make_deposits(200).make_withdrawal(100).make_withdrawal(150).make_withdrawal(23).display_balance()

# BONUS: Add a transfer_money method; have the first user transfer money to the third user and then print both users' balances
Merg.transfer_money(300, Wendy).display_balance
Wendy.display_balance()