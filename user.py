# 

class User:
    def __init__(self, name, bank):
        self.name = name
        self.bank = bank
        self.balance = 0
    
    def make_deposits(self, amount):
        self.balance += amount