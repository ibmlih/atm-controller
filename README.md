# ATM Controller

## File Structure

* `test.py`: The `TestATM` class contains test cases for the files below.

* `controller.py`: The `Controller` class interacts with a `Bank` object to support the following operations: inserting a card, verifying a pin number, selecting an account, getting a balance, depositing, and withdrawing.

* `bank.py`: The `Bank` class stores a list of `Card` objects and their pin numbers.

* `card.py`: The `Card` class stores a list of `Account` objects associated with the card.

* `account.py`: The `Account` class maintains the current balance.

## Run Tests

1. `git clone https://github.com/ibmlih/atm-controller.git`

2. `cd atm-controller/`

3. `python3 test.py`
