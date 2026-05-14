import pytest
from unittest.mock import MagicMock
from fastapi import HTTPException

from backend.services.account_service import AccountService
from backend.models.account import Account, AccountType, AccountCreate
from backend.models.customer import Customer

@pytest.fixture
def mock_repo():
    return MagicMock()

@pytest.fixture
def mock_cust_repo():
    return MagicMock()


@pytest.fixture
def account_service(mock_repo, mock_cust_repo):
    return AccountService(mock_repo, mock_cust_repo)

def test_get_all_accounts(account_service, mock_repo):
    fake_accounts = [
        Account(id=1, customer_id=1, type=AccountType.SAVINGS, balance=500.0),
        Account(id=2, customer_id=2, type=AccountType.CHECKING, balance = 60.0),
    ]
    mock_repo.get_all_account.return_value = fake_accounts

    result = account_service.getAllAccounts()

    assert len(result) == 2
    assert result[0].type == AccountType.SAVINGS
    mock_repo.get_all_account.assert_called_once()

def test_get_account_by_customer_id(account_service, mock_repo):
    fake_accounts = [
        Account(id=1, customer_id=5, type=AccountType.SAVINGS, balance=500.0),
        Account(id=2, customer_id=5, type=AccountType.CHECKING, balance = 60.0),
    ]
    mock_repo.get_accounts_id.return_value = fake_accounts

    result = account_service.getAccountByCustomerID(5)

    assert len(result) == 2
    assert result[0].customer_id == 5
    mock_repo.get_accounts_id.assert_called_once_with(5)

def test_premium_account(account_service, mock_repo):
    fake_accounts = [
        Account(id=1, customer_id=5, type=AccountType.SAVINGS, balance=150000.0),
        Account(id=2, customer_id=3, type=AccountType.CHECKING, balance =200000.0),
    ]
    mock_repo.get_accounts_greater.return_value = fake_accounts

    result = account_service.getPremiumAccount()

    assert len(result) == 2
    assert result[1].balance >= 10000
    mock_repo.get_accounts_greater.assert_called_once_with(10000)

def test_create_account_sucesss(account_service, mock_repo, mock_cust_repo):
    cust_id = 1
    new_account = AccountCreate(type=AccountType.SAVINGS, balance=500.0)

    fake_customer = Customer(id=cust_id, name="John Doe", accounts=[], email="johndoe@example.com")
    mock_cust_repo.get_id_customer.return_value=fake_customer

    expected_account = Account(id=10, customer_id=cust_id, type=AccountType.SAVINGS, balance=500.0)
    mock_repo.create_account.return_value = expected_account

    result = account_service.createAccount(custID=cust_id, newAcc=new_account)

    assert result.id == 10
    assert expected_account in fake_customer.accounts

    mock_repo.create_account.assert_called_once_with(cust_id, new_account)

def test_create_account_negative_balance(account_service, mock_repo):
    cust_id = 1
    new_account = AccountCreate(type=AccountType.SAVINGS, balance=-100.0)

    with pytest.raises(HTTPException) as exc_info:
        account_service.createAccount(custID=cust_id, newAcc=new_account)

    assert exc_info.value.status_code == 400
    assert exc_info.value.detail == "Balance can't be negative"

    mock_repo.create_account.assert_not_called()

def test_create_account_customer_not_found(account_service, mock_repo, mock_cust_repo):
    cust_id = 967
    new_account = AccountCreate(type=AccountType.SAVINGS, balance=500.0)

    mock_cust_repo.get_id_customer.return_value = None

    with pytest.raise(HTTPException) as exc info:
        account_service.createAccount(custId=cust_id, newAcc=new_account)

    assert exc_info.value.status_code == 404
    assert exc_info.value.detail == f"Customer {cust_id} not found"

    mock_repo.createAccount.assert_not_called()