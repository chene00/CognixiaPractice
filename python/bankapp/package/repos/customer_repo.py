from bson import ObjectId
from models.customer import Customer, CustomerCreate

class CustomerRepository:
    # Take in a mock database. Can be replaced with a real database later
    def __init__(self, collection):
        self.collection = collection

    # Define functions that just retrive data from database. Don't care about rules.

    async def get_all_customer(self) -> list[Customer]:
        customers = []
        async for doc in self.collection.find():
            doc["id"] = str(doc.pop("_id"))
            customers.append(Customer(**doc))
        return customers

    async def get_id_customer(self, custID : str) -> Customer:
        try:
            doc = await self.collection.find_one({"_id": ObjectId(custID)})
            if doc:
                doc["id"] = str(doc.pop("_id"))
                return Customer(**doc)
            return None
        except Exception:
            return None

    async def create_customer(self, newCust : CustomerCreate) -> Customer:
        custDict = newCust.model_dump()
        
        result = await self.collection.insert_one(custDict)

        return await self.get_id_customer(str(result.inserted_id))
        