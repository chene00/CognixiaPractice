import pytest
from fastapi.testclient import TestClient
from backend.main import app

# Create a test client
client= TestClient(app)

def test_create_account_api_success():
    cust_id = 1

    payload = {
        "type" : "savings",
        "balance": 1500.00
    }

    response = client.post(f"/api/accounts/{cust_id}", json=payload)

    assert response.status_code == 200
    data = response.json()
    assert data["customer_id"] == cust_id
    assert data["type"] == "savings"
    assert data["balance"] == 1500.00
    assert "id" in data

def test_create_account_api_failure():
    cust_id = 1

    payload = {
        "type" : "savings",
        "balance": -1000.00
    }

    response = client.post(f"/api/accounts/{cust_id}", json=payload)

    assert response.status_code == 400
    data = response.json()
    assert data["detail"] == "Balance can't be negative"

def test_create_account_api_customer_not_found():
    cust_id = 967

    payload = {
        "type" : "savings",
        "balance": 20000.00
    }

    response = client.post(f"/api/accounts/{cust_id}", json=payload)

    assert response.status_code == 404
    data = response.json()
    assert data["detail"] == f"Customer {cust_id} not found"