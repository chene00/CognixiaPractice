from bson import ObjectId
from models.account import AccountType, Account, AccountCreate

class AccountRepository:
    # Take in a mock database. Can be replaced with a real database later
    def __init__(self, collection):
        self.collection = collection

    # Define functions that just retrive data from database. Don't care about rules.
    
    async def get_all_account(self) -> list[Account]:
        accounts = []
        async for doc in self.collection.find():
            doc["id"] = str(doc.pop("_id"))
            accounts.append(Account(**doc))
        return accounts

    async def get_accounts_id(self, custID : str) -> list[Account]:
        cust_accounts = []
        async for doc in self.collection.find({"customer_id": custID}):
            doc["id"] = str(doc.pop("_id"))
            cust_accounts.append(Account(**doc))
        return cust_accounts

    async def get_accounts_greater(self, min_bal : float) -> list[Account]:
        great_accounts = []
        async for doc in self.collection.find({"balance": {"$gte":min_bal}}):
            doc["id"] = str(doc.pop("_id"))
            cust_accounts.append(Account(**doc))
        return great_accounts

    async def create_account(self, custID : str, newAcc : AccountCreate) -> Account:
        accDict = newAcc.model_dump()
        
        accDict["customer_id"] = custID

        result = await self.collection.insert_one(accDict)

        doc = await self.collection.find_one({"_id": result.inserted_id})
        doc["id"] = str(doc.pop("_id"))
        return Account(**doc)
        