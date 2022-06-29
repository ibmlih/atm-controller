from typing import Type
from numpy import isin


class Account:
    def __init__(self):
        self.balance = 0
        
    def get_balance(self):
        return self.balance
    
    def deposit(self, amount):
        if not isinstance(amount, int):
            raise TypeError("amount must be an integer")
        if amount < 0:
            raise ValueError("amount must be positive")
        
        self.balance += amount
        
    def withdraw(self, amount):
        if not isinstance(amount, int):
            raise TypeError("amount must be an integer")
        if amount > self.balance:
            raise ValueError("amount greater than the current balance")
        
        self.balance -= amount