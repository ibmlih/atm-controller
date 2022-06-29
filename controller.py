class Controller:
    def __init__(self, bank):
        """Initializes a Controller object.

        Args:
            bank (Bank): A Bank object that the controller interacts with.
        """
        self.bank = bank
        self.card_number = None
        self.pin_number = None
        self.account_name = None
    
    def insert_card(self, card_number):
        self.card_number = card_number
        return self.bank.is_valid_card(self.card_number)
        
    def enter_pin(self, pin_number):
        self.pin_number = pin_number
        return self.bank.is_correct_pin(self.card_number, self.pin_number)
    
    def select_account(self, account_name):
        self.account_name = account_name
        return self.bank.is_valid_account(self.card_number, self.pin_number, self.account_name)
    
    def get_balance(self):
        return self.bank.get_balance(self.card_number, self.pin_number, self.account_name)
    
    def deposit(self, amount):
        self.bank.deposit(self.card_number, self.pin_number, self.account_name, amount)
    
    def withdraw(self, amount):
        self.bank.withdraw(self.card_number, self.pin_number, self.account_name, amount)
        