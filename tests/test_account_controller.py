import pytest
import pytest_asyncio
from httpx import AsyncClient, ASGITransport
from motor.motor_asyncio import AsyncIOMotorClient

from backend.main import app

# CRITICAL FIX: Import get_current_user directly from the controller namespace 
# so FastAPI overrides the exact same object reference in memory!
from backend.controllers.account_controller import get_database, get_current_user
from backend.models.customer import CustomerResponse


@pytest_asyncio.fixture
async def test_db():
    client = AsyncIOMotorClient("mongodb://localhost:27017")
    db = client["test_bankapp_db"]

    yield db

    await client.drop_database("test_bankapp_db")
    client.close()

@pytest.fixture
def override_get_database(test_db):
    app.dependency_overrides[get_database] = lambda: test_db
    yield
    app.dependency_overrides.clear()

@pytest.mark.asyncio
async def test_create_account_api_success(override_get_database):
    
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
        cust_payload = {
            "name": "Jane Doe",
            "email": "janedone@example.com",
            "password": "password123"
        }
        cust_response = await client.post("/api/customers/", json=cust_payload)
        assert cust_response.status_code == 201

        cust_id = cust_response.json()["id"]

        # Override authentication dynamically
        app.dependency_overrides[get_current_user] = lambda: CustomerResponse(id=cust_id, name="Jane Doe", email="janedone@example.com")

        try:
            acc_payload = {
                "type" : "savings",
                "balance": 1500.00
            }

            response = await client.post(f"/api/accounts/{cust_id}", json=acc_payload)

            assert response.status_code == 201
            data = response.json()
            assert data["customer_id"] == cust_id
            assert data["type"] == "savings"
            assert data["balance"] == 1500.00
            assert "id" in data
        finally:
            app.dependency_overrides.pop(get_current_user, None)

@pytest.mark.asyncio
async def test_create_account_api_failure(override_get_database):

    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
        cust_id = "1"

        # Override authentication dynamically
        app.dependency_overrides[get_current_user] = lambda: CustomerResponse(id=cust_id, name="Test", email="test@test.com")

        try:
            payload = {
                "type" : "savings",
                "balance": -1000.00
            }

            response = await client.post(f"/api/accounts/{cust_id}", json=payload)

            assert response.status_code == 400
            data = response.json()
            assert data["detail"] == "Balance can't be negative"
        finally:
            app.dependency_overrides.pop(get_current_user, None)

@pytest.mark.asyncio
async def test_create_account_api_customer_not_found(override_get_database):
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
        fake_cust_id = "5f8c04b8a9b9a45612345678"

        # Override authentication dynamically
        app.dependency_overrides[get_current_user] = lambda: CustomerResponse(id=fake_cust_id, name="Fake", email="fake@fake.com")

        try:
            payload = {
                "type" : "savings",
                "balance": 20000.00
            }

            response = await client.post(f"/api/accounts/{fake_cust_id}", json=payload)

            assert response.status_code == 404
            data = response.json()
            assert data["detail"] == f"Customer {fake_cust_id} not found"
        finally:
            app.dependency_overrides.pop(get_current_user, None)