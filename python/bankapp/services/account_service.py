from fastapi import HTTPException
from repos.account_repo import AccountRepository
from models.account import Account

class AccountService():
    # Need to pass in the repo in order to retrive data from the database and do operations on them
    def __init__(self, acc_repo: AccountRepository):
        self.repo = acc_repo

    # Define the busniess rules/logic here
    
    def getAllAccounts(self) -> list[Account]:
        return self.repo.get_all_account()

    def getAccountByCustomerID(self, custID : int) -> list[Account]:
        return self.repo.get_accounts_id(custID)

    def getPremiumAccount(self) -> list[Account]:
        return self.repo.get_accounts_greater(10000)