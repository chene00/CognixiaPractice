from fastapi import APIRouter
from models.account import Account
from repos.account_repo import AccountRepository
from services.account_service import AccountService
from db.database import ACCOUNTS

# Create a router specific for accounts
router = APIRouter(prefix="/accounts", tags=["Accounts"])

# Intialize the repo and service
account_repo = AccountRepository(ACCOUNTS)
account_service = AccountService(account_repo)

# Create endpoints for accounts
@router.get("/", response_model=list[Account])
def get_all_accounts(): 
    return account_service.getAllAccounts()

@router.get("/premium", response_model=list[Account])
def get_premium_account():
    return account_service.getPremiumAccount()

@router.get("/{custID}", response_model=list[Account])
def get_account_by_custID(custID : int):
    return account_service.getAccountByCustomerID(custID)