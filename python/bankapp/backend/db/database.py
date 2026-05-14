from models.customer import Customer
from models.account import Account, AccountType

# Make mock Accounts
ACCOUNTS = [
    Account(id=1, customer_id=1, type=AccountType.SAVINGS, balance=5000.00),
    Account(id=2, customer_id=2, type=AccountType.CHECKING, balance=23000.00),
    Account(id=3, customer_id=1, type=AccountType.SAVINGS, balance=87000.00),
    Account(id=4, customer_id=1, type=AccountType.CHECKING, balance=10.00),
    Account(id=5, customer_id=3, type=AccountType.CHECKING, balance=10000.00),
    Account(id=6, customer_id=3, type=AccountType.SAVINGS, balance=200000.00)
]

# Make mock Customers
CUSTOMERS = [
    Customer(id=1, name="John Doe", accounts=[ACCOUNTS[0], ACCOUNTS[2], ACCOUNTS[3]], email="johndoe@example.com"),
    Customer(id=2, name="Jane Doe", accounts=[ACCOUNTS[1]], email="janedoe@example.com"),
    Customer(id=3, name="Timmy Jones", accounts=[ACCOUNTS[4], ACCOUNTS[5]], email="timmyjones@example.com")
]