from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["architecture"] == "monolith"

def test_orders():
    assert client.get("/orders").status_code == 200
