from models.account import AccountType, Account
from db.database import ACCOUNTS, CUSTOMERS

class AccountRepository:
    # Take in a mock database. Can be replaced with a real database later
    def __init__(self, db_accounts: list):
        self.db = db_accounts

    # Define functions that just retrive data from database. Don't care about rules.
    
    def get_all_account(self):
        return self.db

    def get_accounts_id(self, id : int):
        cust_accounts = []
        for acc in self.db:
            if acc.customer_id == id:
                cust_accounts.append(acc)
        
        return cust_accounts

    def get_accounts_greater(self, min_bal : float):
        great_accounts = []
        for acc in self.db:
            if acc.balance >= min_bal:
                great_accounts.append(acc)
        
        return great_accounts