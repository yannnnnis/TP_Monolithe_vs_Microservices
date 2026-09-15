from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_payment():
    response = client.post("/payments", json={"order_id": 10, "amount": 100})
    assert response.status_code == 200
    assert response.json()["status"] == "authorized"
