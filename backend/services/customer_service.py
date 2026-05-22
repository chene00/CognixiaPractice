from fastapi import HTTPException
from repos.customer_repo import CustomerRepository
from models.customer import Customer, CustomerCreate, CustomerResponse
from utils.auth import get_password_hash

class CustomerService():
    # Need to pass in the repo in order to retrive data from the database and do operations on them
    def __init__(self, cust_repo: CustomerRepository):
        self.repo = cust_repo

    # Define the busniess rules/logic here

    async def getAllCustomers(self) -> list[Customer]:
        return await self.repo.get_all_customer()

    async def getCustomerByID(self, custID : str) -> CustomerResponse:
        target = await self.repo.get_id_customer(custID)

        # Example of a rule. 
        
        if target == None:
            raise HTTPException(status_code=404, detail=f"Customer {custID} not found")

        return CustomerResponse(
            id=target.id,
            name=target.name,
            email=target.email
        )

    async def createCustomer(self, newCust : CustomerCreate) -> CustomerResponse:

        all_cust = await self.repo.get_all_customer()

        for customer in all_cust:
            if newCust.email == customer.email:
                raise HTTPException(status_code=400, detail=f"Email already exist")
            
        hashed_pw = get_password_hash(newCust.password)

        db_customer = Customer(
            name=newCust.name,
            email=newCust.email,
            hashed_password=hashed_pw
        )

        return await self.repo.create_customer(db_customer)