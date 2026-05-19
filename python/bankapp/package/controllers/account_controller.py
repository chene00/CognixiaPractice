from fastapi import APIRouter, Depends
from models.account import Account, AccountCreate
from repos.account_repo import AccountRepository
from repos.customer_repo import CustomerRepository
from services.account_service import AccountService
from db.mongodb import get_database

# Create a router specific for accounts
router = APIRouter(prefix="/accounts", tags=["Accounts"])


def get_account_service(db = Depends(get_database)):

    customer_collection = db["customers"]
    account_collection = db["accounts"]

    acc_repo = AccountRepository(account_collection)
    cust_repo = CustomerRepository(customer_collection)

    return AccountService(acc_repo, cust_repo)

# Create endpoint for account
@router.get("/", response_model=list[Account])
async def get_all_accounts(service : AccountService = Depends(get_account_service)): 
    return await service.getAllAccounts()

@router.get("/premium", response_model=list[Account])
async def get_premium_account(service : AccountService = Depends(get_account_service)):
    return await service.getPremiumAccount()

@router.get("/{custID}", response_model=list[Account])
async def get_account_by_custID(custID : str, service : AccountService = Depends(get_account_service)):
    return await service.getAccountByCustomerID(custID)

@router.post("/{custID}", response_model=Account, status_code=201)
async def create_account(custID : str, newAcc : AccountCreate, service : AccountService = Depends(get_account_service)):
    return await service.createAccount(custID, newAcc)