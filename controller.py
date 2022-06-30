class Controller:
    def __init__(self, bank):
        """Initialize a Controller object.

        Args:
            bank (Bank): A Bank object that the controller interacts with.
            
        Member Variables:
            self.bank (Bank): a Bank object
            self.card_number (int): stores a card number of an inserted card
            self.pin_number (str): stores a pin number of an inserted card
            self.account_name (str): stores a selected account name
        """
        self.bank = bank
        self.card_number = None
        self.pin_number = None
        self.account_name = None
    
    def insert_card(self, card_number):
        """Insert a card into an ATM.

        Args:
            card_number (int): number of a card to be inserted

        Returns:
            bool: Return True if card_number is successfully inserted. 
                  Otherwise, return False.
        """
        self.card_number = card_number
        return self.bank.is_valid_card(self.card_number)
        
    def verify_pin(self, pin_number):
        """Verify a pin number for the inserted card.

        Args:
            pin_number (str): pin number for the inserted card

        Returns:
            bool: Return True if pin_number matches the pin number for the
                  inserted card. Otherwise, return False.
        """
        self.pin_number = pin_number
        return self.bank.is_correct_pin(self.card_number, self.pin_number)
    
    def select_account(self, account_name):
        """Select an account from the card to check balance, deposit, or withdraw.

        Args:
            account_name (str): name of an account to select

        Returns:
            bool: Return True if account_name is successfully selected.
                  Otherwise, return False.
        """
        self.account_name = account_name
        return self.bank.is_valid_account(self.card_number, self.pin_number, self.account_name)
    
    def get_balance(self):
        """Get the total balance of an account.

        Returns:
            int: total balance in dollars
        """
        return self.bank.get_balance(self.card_number, self.pin_number, self.account_name)
    
    def deposit(self, amount):
        """Deposit money to an account.

        Args:
            amount (int): amount of money to deposit in dollars
        """
        self.bank.deposit(self.card_number, self.pin_number, self.account_name, amount)
    
    def withdraw(self, amount):
        """Withdraw money from an account.

        Args:
            amount (int): amount of money to withdraw in dollars
        """
        self.bank.withdraw(self.card_number, self.pin_number, self.account_name, amount)
        