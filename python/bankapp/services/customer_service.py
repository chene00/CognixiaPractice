from fastapi import HTTPException
from repos.customer_repo import CustomerRepository
from models.customer import Customer

class CustomerService():
    # Need to pass in the repo in order to retrive data from the database and do operations on them
    def __init__(self, cust_repo: CustomerRepository):
        self.repo = cust_repo

    # Define the busniess rules/logic here

    def getAllCustomers(self) -> list[Customer]:
        return self.repo.get_all_customer()

    def getCustomerByID(self, custID : int) -> Customer:
        target = self.repo.get_id_customer(custID)

        # Example of a rule. 
        
        if target == None:
            raise HTTPException(status_code=404, detail=f"Customer {custID} not found")
        else:
            return target

    