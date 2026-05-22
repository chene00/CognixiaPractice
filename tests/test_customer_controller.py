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
        await client.post("/api/customers/", json={"name":"User One", "email":"one@example.com"})
        await client.post("/api/customers/", json={"name":"User TWo", "email":"two@example.com"})

        response = await client.get("/api/customers/")

        assert response.status_code == 200
        assert len(response.json()) >= 2

@pytest.mark.asyncio
async def test_get_customer_by_id_api(override_get_database):
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
        payload = {"name" : "Jane Doe", "email" : "janedoe@example.com"}
        create_reponse = await client.post("/api/customers/", json=payload)
        cust_id = create_response.json()["id"]

        response = await client.get(f"/api/customers/{cust_id}")

        assert response.status_code == 200
        assert response_json.()["name"] == "Jane Doe"

# Continue to add more test