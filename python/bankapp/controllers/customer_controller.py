from fastapi import APIRouter
from models.customer import Customer
from repos.customer_repo import CustomerRepository
from services.customer_service import CustomerService
from db.database import CUSTOMERS

# Create a router specific for customers
router = APIRouter(prefix="/customers", tags=["Customers"])

# Intialize the repo and service
customer_repo = CustomerRepository(CUSTOMERS)
customer_service = CustomerService(customer_repo)

# Create endpoints for customers
@router.get("/", response_model=list[Customer])
def get_all_customers():
    return customer_service.getAllCustomers()

@router.get("/{custID}", response_model=Customer)
def get_customer_by_id(custID : int):
    return customer_service.getCustomerByID(custID)
