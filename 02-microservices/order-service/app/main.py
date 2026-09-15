from fastapi import FastAPI
import os
import requests

app = FastAPI(title="ShopDemo Order Service")
PAYMENT_URL = os.getenv("PAYMENT_URL", "http://payment-service:8002")

@app.get("/")
def home():
    return {"service": "order-service", "architecture": "microservices"}

@app.get("/orders")
def orders():
    return {"service": "order-service"}

@app.post("/orders/{order_id}/pay")
def pay(order_id: int):
    response = requests.post(
        f"{PAYMENT_URL}/payments",
        json={"order_id": order_id, "amount": 100}
    )
    return {"order_id": order_id, "payment": response.json()}
