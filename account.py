class Account:
    def __init__(self, name):
        """Initialize an Account object.

        Args:
            name (str): account name
        
        Member Variables:
            self.name (str): account name
            self.balance (int): current balance
        """
        self.name = name
        self.balance = 0
        
    def get_name(self):
        """Get an account name.

        Returns:
            str: account name
        """
        return self.name
        
    def get_balance(self):
        """Get the current balance.

        Returns:
            int: current balance in dollars
        """
        return self.balance
    
    def deposit(self, amount):
        """Deposit money.

        Args:
            amount (int): amount of money to deposit in dollars

        Raises:
            TypeError: amount must be an integer
            ValueError: amount must be positive
        """
        if not isinstance(amount, int):
            raise TypeError("amount must be an integer")
        if amount < 0:
            raise ValueError("amount must be positive")
        
        self.balance += amount
        
    def withdraw(self, amount):
        """Withdraw money.

        Args:
            amount (int): amount of money to withdraw in dollars

        Raises:
            TypeError: amount must be an integer
            ValueError: amount must be positive
            ValueError: amount greater than the current balance
        """
        if not isinstance(amount, int):
            raise TypeError("amount must be an integer")
        if amount < 0:
            raise ValueError("amount must be positive")
        if amount > self.balance:
            raise ValueError("amount greater than the current balance")
        
        self.balance -= amount
