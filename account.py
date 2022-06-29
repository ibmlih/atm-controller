class Account:
    def __init__(self, name):
        self.name = name
        self.balance = 0
        
    def get_name(self):
        return self.name
        
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
        if amount < 0:
            raise ValueError("amount must be positive")
        if amount > self.balance:
            raise ValueError("amount greater than the current balance")
        
        self.balance -= amount
