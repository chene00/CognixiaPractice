from fastapi import HTTPException
from repos.account_repo import AccountRepository
from repos.customer_repo import CustomerRepository
from models.account import Account, AccountCreate

class AccountService():
    # Need to pass in the repo in order to retrive data from the database and do operations on them
    def __init__(self, acc_repo: AccountRepository, cust_repo: CustomerRepository):
        self.repo = acc_repo
        self.cust_repo = cust_repo

    # Define the busniess rules/logic here
    
    async def getAllAccounts(self) -> list[Account]:
        return await self.repo.get_all_account()

    async def getPremiumAccount(self) -> list[Account]:
        return await self.repo.get_accounts_greater(10000)

    async def getAccountByCustomerID(self, request_custID : str, current_custID : str) -> list[Account]:
        if request_custID != current_custID:
            raise HTTPException(status_code=403, detail="Not authorized to view these accounts")

        return await self.repo.get_accounts_id(request_custID)

    async def createAccount(self, request_custID : str, newAcc : AccountCreate, current_custID : str) -> Account:
        if request_custID != current_custID:
            raise HTTPException(status_code=403, detail="Not authorized to modify this user")

        if newAcc.balance < 0:
            raise HTTPException(status_code=400, detail="Balance can't be negative")

        customer = await self.cust_repo.get_id_customer(request_custID)
        if not customer:
            raise HTTPException(status_code=404, detail=f"Customer {request_custID} not found")
    
        return await self.repo.create_account(request_custID, newAcc)
        