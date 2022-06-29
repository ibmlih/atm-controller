import account

class Card:
    def __init__(self, number):
        self.number = number
        self.accounts = {} # name -> Account()
        
    def get_number(self):
        return self.number
    
    def add_account(self, name):
        if name in self.accounts:
            raise ValueError("account already exists")
        
        self.accounts[name] = account.Account(name)
    
    def is_valid_account(self, name):
        return name in self.accounts
    
    def get_balance(self, name):
        return self.accounts[name].get_balance()
    
    def deposit(self, name, amount):
        self.accounts[name].deposit(amount)
    
    def withdraw(self, name, amount):
        self.accounts[name].withdraw(amount)
