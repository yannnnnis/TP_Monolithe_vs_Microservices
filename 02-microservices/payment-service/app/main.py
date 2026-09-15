from fastapi import FastAPI

app = FastAPI(title="ShopDemo Payment Service")

@app.get("/")
def home():
    return {"service": "payment-service", "architecture": "microservices"}

@app.post("/payments")
def payment(payload: dict):
    return {
        "status": "authorized",
        "order_id": payload.get("order_id"),
        "amount": payload.get("amount")
    }
