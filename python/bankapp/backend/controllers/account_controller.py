from fastapi import APIRouter
from models.account import Account, AccountCreate
from repos.account_repo import AccountRepository
from repos.customer_repo import CustomerRepository
from services.account_service import AccountService
from db.database import ACCOUNTS, CUSTOMERS

# Create a router specific for accounts
router = APIRouter(prefix="/accounts", tags=["Accounts"])

# Intialize the repo and service
account_repo = AccountRepository(ACCOUNTS)
customer_repo = CustomerRepository(CUSTOMERS)
account_service = AccountService(account_repo, customer_repo)

# Create endpoint for account
@router.get("/", response_model=list[Account])
def get_all_accounts(): 
    return account_service.getAllAccounts()

@router.get("/premium", response_model=list[Account])
def get_premium_account():
    return account_service.getPremiumAccount()

@router.get("/{custID}", response_model=list[Account])
def get_account_by_custID(custID : int):
    return account_service.getAccountByCustomerID(custID)

@router.post("/{custID}", response_model=Account)
def create_account(custID : int, newAcc : AccountCreate):
    return account_service.createAccount(custID, newAcc)