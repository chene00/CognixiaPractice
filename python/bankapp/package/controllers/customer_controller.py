from fastapi import APIRouter, Depends
from models.customer import Customer, CustomerCreate
from repos.customer_repo import CustomerRepository
from services.customer_service import CustomerService
from db.mongodb import get_database

# Create a router specific for customers
router = APIRouter(prefix="/customers", tags=["Customers"])

# Have it create a new service at each call. Fixes State Leakage
def get_customer_service(db = Depends(get_database)):
    customer_collection = db["customers"]
    repo = CustomerRepository(customer_collection)
    return CustomerService(repo)

# Create endpoints for customers
@router.get("/", response_model=list[Customer])
# Async tells python that this tasks might require some waiting. Can pause it if needed
# Depends makes it so it will automatically call the function for you
async def get_all_customers(service : CustomerService = Depends(get_customer_service)):
    # Actual pause button
    return await service.getAllCustomers()

@router.get("/{custID}", response_model=Customer)
async def get_customer_by_id(custID : str, service : CustomerService = Depends(get_customer_service)):
    return await service.getCustomerByID(custID)

@router.post("/", response_model=Customer, status_code=201)
async def create_customer(newCust : CustomerCreate, service : CustomerService = Depends(get_customer_service)):
    return await service.createCustomer(newCust)