"""
Basic Exercise: Creating a "Person" Class
Objectives:
Implement a class with constructors, attributes, and methods.
Demonstrate object instantiation and method usage.
Exercise:
Create a class Person with the following attributes:

name (string)
age (integer)
location (string)
Implement the following methods:

__init__: A constructor to initialize a person's name, age, and location.
introduce: A method that prints a friendly introduction like: "Hi, I'm [name], [age] years old, from [location]."
Instantiate two Person objects with different attributes and call their introduce methods.
"""


class Person:
    # constructor class (s)
    def __init__(self, name: str, age: int, location: str) -> None:
        self.name = name
        self.age = age
        self.location = location

    # instance method that takes positional arguments
    def introduce(self) -> str:
        return f"Hi, I'm {self.name}, {self.age} years old, from {self.location}"


intro1 = Person("Robert", 35, "Los Angeles")
intro2 = Person("Kimberly", 31, "Los Angeles")
print(intro1.introduce())
print(intro2.introduce())
print("\n")


"""
Advanced Challenge: Implementing a "Bank Account" Class
Objectives:
Create a class with private attributes, validation, and multiple methods.
Use more advanced techniques like input validation, getters, setters, and static methods.
Challenge:
Create a class BankAccount with the following attributes:

account_holder (string)
balance (private float, initialized to 0.0)
account_number (string)
Implement the following methods:

__init__: A constructor to initialize the account holder, account number, and optional initial balance.
deposit(amount): A method to increase the balance. Validate that amount is a positive number.
withdraw(amount): A method to decrease the balance. Ensure that amount is a positive number and less than or equal to the current balance.
get_balance(): A method to return the current balance.
set_balance(amount): A method to set the balance to a specific value (optional for testing purposes).
transfer(amount, recipient_account): A method to transfer a specified amount to another BankAccount object. Validate the amount before transferring.
__str__: A method that returns a string representation of the account (e.g., "Account: [account_number], Holder: [account_holder], Balance: $[balance]").
Add a static method validate_account_number(account_number) that checks if an account number is valid (e.g., 10 numeric digits).

Test the class:

Create two BankAccount objects.
Deposit money into one account.
Withdraw money from one account.
Transfer money between the two accounts.
Print the details of both accounts.
"""

# Solution:
# BankAccount class implementation with validation and private attributes
class BankAccount:
    # Static method to validate account numbers are 10 digits
    @staticmethod
    def validate_account_number(account_number: str) -> bool:
        try:
            if len(account_number) != 10 or not account_number.isdigit():
                raise ValueError("Account number must be exactly 10 digits")
            return True
        except Exception as e:
            raise ValueError(f"Invalid account number: {str(e)}")

    # Constructor to initialize account with holder name, number and optional balance
    def __init__(self, account_holder: str, account_number: str, initial_balance: float = 0.0) -> None:
        if not self.validate_account_number(account_number):
            raise ValueError("Invalid account number. Must be 10 digits.")
        self.account_holder = account_holder
        self.__balance = float(initial_balance)  # Private balance attribute
        self.account_number = account_number

    # Method to deposit money, validates positive amount
    def deposit(self, amount: float) -> bool:
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.__balance += amount
        return True

    # Method to withdraw money, validates amount is positive and sufficient funds exist
    def withdraw(self, amount: float) -> bool:
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self.__balance:
            raise ValueError("Insufficient funds")
        self.__balance -= amount
        return True

    # Getter method to access private balance
    def get_balance(self) -> float:
        return self.__balance

    # Setter method to modify private balance (for testing)
    def set_balance(self, amount: float) -> None:
        self.__balance = float(amount)

    # Method to transfer money between accounts with validation
    def transfer(self, amount: float, recipient_account: "BankAccount") -> bool:
        if not isinstance(recipient_account, BankAccount):
            raise ValueError("Recipient must be a BankAccount object")
        self.withdraw(amount)  # This will validate the withdrawal
        recipient_account.deposit(amount)
        return True

    # String representation of account details
    def __str__(self) -> str:
        return f"Account: {self.account_number}, Holder: {self.account_holder}, Balance: ${self.__balance:.2f}"


# Create example accounts
account_a = BankAccount("Alice Smith", "1111222233", 1000.00)
account_b = BankAccount("Bob Jones", "4444555566", 500.00)

# Demonstrate deposit
print("\nTesting deposit:")
account_a.deposit(250.50)
print(f"After depositing $250.50: {account_a}")

# Demonstrate withdrawal 
print("\nTesting withdrawal:")
account_a.withdraw(100.00)
print(f"After withdrawing $100.00: {account_a}")

# Demonstrate balance getter
print("\nTesting get_balance:")
print(f"Current balance for {account_a.account_holder}: ${account_a.get_balance():.2f}")

# Demonstrate balance setter
print("\nTesting set_balance:")
account_a.set_balance(2000.00)
print(f"After setting balance to $2000.00: {account_a}")

# Demonstrate transfer
print("\nTesting transfer:")
print(f"Before transfer - {account_a}")
print(f"Before transfer - {account_b}")
account_a.transfer(500.00, account_b)
print(f"After transferring $500.00:")
print(f"Sender account - {account_a}")
print(f"Recipient account - {account_b}")

# Demonstrate string representation
print("\nTesting string representation:")
print(account_a)
print(account_b)


# Example usage and test cases:
def test_bank_account() -> None:
    # Create test accounts
    # Account 1: Valid 10-digit account number
    account1 = BankAccount("James Wilson", "1234567890", 1000)
    # Account 2: Invalid account number to test validation
    account2 = BankAccount("Sarah Johnson", "45", -500)
    # Account 3: Single name to test name validation
    account3 = BankAccount("Robert", "9876543210", 4500)
    # Account 4: over withdrawal test
    account4 = BankAccount("Mary Smith", "1112223334", 100)
    # Account 5: insufficient fund transfer test
    account5 = BankAccount("John Doe", "5556667778", 50)

    # Test deposit functionality
    assert account1.get_balance() == 1000
    account1.deposit(500)
    assert account1.get_balance() == 1500

    assert account2.get_balance() == 0
    account2.deposit(200)
    assert account2.get_balance() == 200

    assert account3.get_balance() == 4500
    account3.deposit(4500)
    assert account3.get_balance() == 9000

    # Test withdrawal functionality
    account1.withdraw(300)
    assert account1.get_balance() == 1200

    account2.withdraw(20)
    assert account2.get_balance() == 180

    # This should raise ValueError for insufficient funds
    try:
        account3.withdraw(4600)
        assert False, "Should have raised ValueError"
    except ValueError:
        pass

    # Test over withdrawal
    try:
        account4.withdraw(200)  # Trying to withdraw more than balance of 100
        assert False, "Should have raised ValueError"
    except ValueError:
        pass

    # Test transfer between accounts
    account1.transfer(500, account2)
    assert account1.get_balance() == 700
    assert account2.get_balance() == 680

    # Test insufficient funds transfer
    try:
        account5.transfer(100, account1)  # Trying to transfer more than balance of 50
        assert False, "Should have raised ValueError"
    except ValueError:
        pass

    # This should raise ValueError for negative amount
    try:
        account2.transfer(-300, account1)
        assert False, "Should have raised ValueError"
    except ValueError:
        pass

    print("All tests passed!")


# Run the tests
# test_bank_account()