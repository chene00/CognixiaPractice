import pytest
from unittest.mock import AsyncMock
from fastapi import HTTPException

from backend.services.customer_service import CustomerService
from backend.models.customer import Customer

@pytest.fixture
def mock_repo():
    return AsyncMock()

@pytest.fixture
def customer_service(mock_repo):
    return CustomerService(mock_repo)

@pytest.mark.asyncio
async def test_get_all_customers(customer_service, mock_repo):
    fake_customers = [
        # Added hashed_password
        Customer(id="1", name="Alice Jones", email="alicejones@example.com", hashed_password="pw"),
        Customer(id="2", name="Bob Henry", email="bobhenery@example.com", hashed_password="pw")
    ]
    
    mock_repo.get_all_customer.return_value = fake_customers

    result = await customer_service.getAllCustomers()

    assert len(result) == 2
    assert result[0].name == "Alice Jones"
    mock_repo.get_all_customer.assert_called_once()

@pytest.mark.asyncio
async def test_get_customer_by_id(customer_service, mock_repo):
    # Added hashed_password
    fake_customer = Customer(id="99", name="John Doe", email="johndoe@example.com", hashed_password="pw")
    mock_repo.get_id_customer.return_value = fake_customer

    result = await customer_service.getCustomerByID("99")
    assert result.id == "99"
    assert result.name == "John Doe"
    mock_repo.get_id_customer.assert_called_once_with("99")

@pytest.mark.asyncio
async def test_get_customer_by_id_not_found(customer_service, mock_repo):
    mock_repo.get_id_customer.return_value = None

    with pytest.raises(HTTPException) as exc_info:
        await customer_service.getCustomerByID("1")

    assert exc_info.value.status_code == 404
    assert exc_info.value.detail == "Customer 1 not found"
    mock_repo.get_id_customer.assert_called_once_with("1")