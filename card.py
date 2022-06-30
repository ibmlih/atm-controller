import account

class Card:
    def __init__(self, number):
        """Initialize a Card object.

        Args:
            number (int): number of a card
        
        Member Variables:
            self.number (int): number of a card
            self.accounts (dict): dictionary that maps an account name (str) to an Account object.
        """
        self.number = number
        self.accounts = {}
        
    def get_number(self):
        """Get a card number.

        Returns:
            int: a card number
        """
        return self.number
    
    def add_account(self, name):
        """Add an account to a card.

        Args:
            name (str): name of an account to add

        Raises:
            ValueError: account already exists
        """
        if name in self.accounts:
            raise ValueError("account already exists")
        
        self.accounts[name] = account.Account(name)
    
    def is_valid_account(self, name):
        """Check if an account exists under a card.

        Args:
            name (str): name of an account to check

        Returns:
            bool: Return True if an account exists under a card.
                  Otherwise, return False.
        """
        return name in self.accounts
    
    def get_balance(self, name):
        """Get the total balance of an account.

        Args:
            name (str): name of an account to check

        Returns:
            int: total balance of an account in dollars
        """
        return self.accounts[name].get_balance()
    
    def deposit(self, name, amount):
        """Deposit money to an account.

        Args:
            name (str): name of an account to deposit
            amount (int): amount of money to deposit in dollars
        """
        self.accounts[name].deposit(amount)
    
    def withdraw(self, name, amount):
        """Withdraw money from an account.

        Args:
            name (str): name of an account to withdraw
            amount (int): amount of money to withdraw in dollars
        """
        self.accounts[name].withdraw(amount)
