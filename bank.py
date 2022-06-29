import card

class Bank:
    def __init__(self):
        self.card = {} # number -> card
        self.pin = {} # number -> pin
    
    def add_card(self, card_number, pin_number):
        if card_number in self.card:
            raise ValueError("card_number already exists")
        
        self.card[card_number] = card.Card(card_number)
        self.pin[card_number] = pin_number
        
    def add_account(self, card_number, pin_number, name):
        if card_number not in self.card:
            raise ValueError("card_number not added to the bank")
        if self.pin[card_number] != pin_number:
            raise ValueError("pin_number is incorrect")
        
        self.card[card_number].add_account(name)        
        
    def is_valid_card(self, card_number):
        return card_number in self.card
    
    def is_correct_pin(self, card_number, pin_number):
        return self.is_valid_card(card_number) and self.pin[card_number] == pin_number
    
    def is_valid_account(self, card_number, pin_number, account_name):
        return (self.is_correct_pin(card_number, pin_number) and 
                self.card[card_number].is_valid_account(account_name))
    
    def get_balance(self, card_number, pin_number, account_name):
        if not self.is_valid_account(card_number, pin_number, account_name):
            raise ValueError("unable to get balance")
        
        return self.card[card_number].get_balance(account_name)
    
    def deposit(self, card_number, pin_number, account_name, amount):
        if not self.is_valid_account(card_number, pin_number, account_name):
            raise ValueError("unable to deposit")

        self.card[card_number].deposit(account_name, amount)

    def withdraw(self, card_number, pin_number, account_name, amount):
        if not self.is_valid_account(card_number, pin_number, account_name):
            raise ValueError("unable to withdraw")

        self.card[card_number].withdraw(account_name, amount)
