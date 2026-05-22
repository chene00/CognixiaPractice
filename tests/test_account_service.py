import pytest
from unittest.mock import AsyncMock
from fastapi import HTTPException

from backend.services.account_service import AccountService
from backend.models.account import Account, AccountType, AccountCreate
from backend.models.customer import Customer

@pytest.fixture
def mock_repo():
    return AsyncMock()

@pytest.fixture
def mock_cust_repo():
    return AsyncMock()

@pytest.fixture
def account_service(mock_repo, mock_cust_repo):
    return AccountService(mock_repo, mock_cust_repo)

@pytest.mark.asyncio
async def test_get_all_accounts(account_service, mock_repo):
    fake_accounts = [
        Account(id="1", customer_id="1", type=AccountType.SAVINGS, balance=500.0),
        Account(id="2", customer_id="2", type=AccountType.CHECKING, balance = 60.0),
    ]
    mock_repo.get_all_account.return_value = fake_accounts

    result = await account_service.getAllAccounts()

    assert len(result) == 2
    assert result[0].type == AccountType.SAVINGS
    mock_repo.get_all_account.assert_called_once()

@pytest.mark.asyncio
async def test_get_account_by_customer_id(account_service, mock_repo):
    fake_accounts = [
        Account(id="1", customer_id="5", type=AccountType.SAVINGS, balance=500.0),
        Account(id="2", customer_id="5", type=AccountType.CHECKING, balance = 60.0),
    ]
    mock_repo.get_accounts_id.return_value = fake_accounts

    # Added 2nd argument current_custID
    result = await account_service.getAccountByCustomerID("5", "5") 

    assert len(result) == 2
    mock_repo.get_accounts_id.assert_called_once_with("5")

@pytest.mark.asyncio
async def test_premium_account(account_service, mock_repo):
    fake_accounts = [
        Account(id="1", customer_id="5", type=AccountType.SAVINGS, balance=150000.0),
        Account(id="2", customer_id="3", type=AccountType.CHECKING, balance =200000.0),
    ]
    mock_repo.get_accounts_greater.return_value = fake_accounts

    result = await account_service.getPremiumAccount()

    assert len(result) == 2
    assert result[1].balance >= 10000
    mock_repo.get_accounts_greater.assert_called_once_with(10000)

@pytest.mark.asyncio
async def test_create_account_sucesss(account_service, mock_repo, mock_cust_repo):
    cust_id = "1"
    new_account = AccountCreate(type=AccountType.SAVINGS, balance=500.0)

    # Added hashed_password
    fake_customer = Customer(id=cust_id, name="John Doe", email="johndoe@example.com", hashed_password="pw")
    mock_cust_repo.get_id_customer.return_value=fake_customer

    expected_account = Account(id="10", customer_id=cust_id, type=AccountType.SAVINGS, balance=500.0)
    mock_repo.create_account.return_value = expected_account

    # Updated keyword arguments
    result = await account_service.createAccount(request_custID=cust_id, newAcc=new_account, current_custID=cust_id)

    assert result.id == "10"
    mock_repo.create_account.assert_called_once_with(cust_id, new_account)

@pytest.mark.asyncio
async def test_create_account_negative_balance(account_service, mock_repo):
    cust_id = "1"
    new_account = AccountCreate(type=AccountType.SAVINGS, balance=-100.0)

    with pytest.raises(HTTPException) as exc_info:
        # Updated keyword arguments
        await account_service.createAccount(request_custID=cust_id, newAcc=new_account, current_custID=cust_id)

    assert exc_info.value.status_code == 400
    assert exc_info.value.detail == "Balance can't be negative"

    mock_repo.create_account.assert_not_called()

@pytest.mark.asyncio
async def test_create_account_customer_not_found(account_service, mock_repo, mock_cust_repo):
    cust_id = "967"
    new_account = AccountCreate(type=AccountType.SAVINGS, balance=500.0)

    mock_cust_repo.get_id_customer.return_value = None

    with pytest.raises(HTTPException) as exc_info:
        # Updated keyword arguments
        await account_service.createAccount(request_custID=cust_id, newAcc=new_account, current_custID=cust_id)

    assert exc_info.value.status_code == 404
    assert exc_info.value.detail == f"Customer {cust_id} not found"

    mock_repo.create_account.assert_not_called()