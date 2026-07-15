import pytest
from app import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_get_items(client):
    response = client.get("/api/items")
    assert response.status_code == 200
    assert "ITEM001" in response.json

def test_reduce_stock_success(client):
    response = client.post("/api/items/ITEM001/reduce", json={"quantity": 5})
    assert response.status_code == 200

def test_reduce_stock_item_not_found(client):
    response = client.post("/api/items/ITEM999/reduce", json={"quantity": 1})
    assert response.status_code == 404

def test_health_check(client):
    response = client.get("/health")
    assert response.json["status"] == "ok"