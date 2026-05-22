import pytest
import pytest_asyncio
from httpx import AsyncClient, ASGITransport
from motor.motor_asyncio import AsyncIOMotorClient

from backend.main import app
from backend.controllers.customer_controller import get_database

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
async def test_get_all_customer_api(override_get_database):
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
        # Added passwords here
        await client.post("/api/customers/", json={"name":"User One", "email":"one@example.com", "password":"password123"})
        await client.post("/api/customers/", json={"name":"User TWo", "email":"two@example.com", "password":"password123"})

        response = await client.get("/api/customers/")

        assert response.status_code == 200
        assert len(response.json()) >= 2

@pytest.mark.asyncio
async def test_get_customer_by_id_api(override_get_database):
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
        # Added password here
        payload = {"name" : "Jane Doe", "email" : "janedoe@example.com", "password":"password123"}
        create_response = await client.post("/api/customers/", json=payload)
        cust_id = create_response.json()["id"]

        response = await client.get(f"/api/customers/{cust_id}")

        assert response.status_code == 200
        assert response.json()["name"] == "Jane Doe"