import card

class Bank:
    def __init__(self):
        """Initialze a Bank object.
        
        Member Variables:
            self.card (dict): dictionary that maps from a card number (int) to a Card object
            self.pin (dict): dictionary that maps from a card number (int) to its pin number (str)
        """
        self.card = {}
        self.pin = {}
    
    def add_card(self, card_number, pin_number):
        """Add a card and its pin number to the bank.

        Args:
            card_number (int): number of a card to add
            pin_number (str): pin number of a card

        Raises:
            ValueError: card_number already exists
        """
        if card_number in self.card:
            raise ValueError("card_number already exists")
        
        self.card[card_number] = card.Card(card_number)
        self.pin[card_number] = pin_number
        
    def add_account(self, card_number, pin_number, name):
        """Add an account to a card.

        Args:
            card_number (int): number of a card
            pin_number (str): pin number of a card
            name (str): name of an account to add

        Raises:
            ValueError: card_number not added to the bank
            ValueError: pin_number is incorrect
        """
        if card_number not in self.card:
            raise ValueError("card_number not added to the bank")
        if self.pin[card_number] != pin_number:
            raise ValueError("pin_number is incorrect")
        
        self.card[card_number].add_account(name)        
        
    def is_valid_card(self, card_number):
        """Check if a card exists in the bank.

        Args:
            card_number (int): number of a card to check

        Returns:
            bool: Return True if a card exists. 
                  Otherwise, return False.
        """
        return card_number in self.card
    
    def is_correct_pin(self, card_number, pin_number):
        """Check if pin_number is the correct pin number for card_number.
        
        Args:
            card_number (int): number of a card
            pin_number (str): pin number of a card to check

        Returns:
            bool: Return True if pin_number is correct.
                  Otherwise, return False.
        """
        return self.is_valid_card(card_number) and self.pin[card_number] == pin_number
    
    def is_valid_account(self, card_number, pin_number, account_name):
        """Check if an account exists under a card.

        Args:
            card_number (int): number of a card
            pin_number (str): pin number of a card
            account_name (str): name of an account to check

        Returns:
            bool: Return True if account_name exists under a card.
                  Otherwise, return False.
        """
        return (self.is_correct_pin(card_number, pin_number) and 
                self.card[card_number].is_valid_account(account_name))
    
    def get_balance(self, card_number, pin_number, account_name):
        """Get the total balance of an account.

        Args:
            card_number (int): number of a card
            pin_number (str): pin number of a card
            account_name (str): name of an account to check

        Raises:
            ValueError: account is not valid

        Returns:
            int: total balance of an account in dollars
        """
        if not self.is_valid_account(card_number, pin_number, account_name):
            raise ValueError("account is not valid")
        
        return self.card[card_number].get_balance(account_name)
    
    def deposit(self, card_number, pin_number, account_name, amount):
        """Deposit money to an account.

        Args:
            card_number (int): number of a card
            pin_number (str): pin number of a card
            account_name (str): name of an account to deposit
            amount (int): amount of money to deposit in dollars

        Raises:
            ValueError: account is not valid
        """
        if not self.is_valid_account(card_number, pin_number, account_name):
            raise ValueError("account is not valid")

        self.card[card_number].deposit(account_name, amount)

    def withdraw(self, card_number, pin_number, account_name, amount):
        """Withdraw money from an account.

        Args:
            card_number (int): number of card
            pin_number (str): pin number of card
            account_name (str): name of an account to withdraw
            amount (int): amount of money to withdraw in dollars

        Raises:
            ValueError: account is not valid
        """
        if not self.is_valid_account(card_number, pin_number, account_name):
            raise ValueError("account is not valid")

        self.card[card_number].withdraw(account_name, amount)
