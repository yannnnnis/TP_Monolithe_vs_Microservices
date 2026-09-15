from fastapi import FastAPI

app = FastAPI(title="ShopDemo Monolith")

@app.get("/")
def home():
    return {"architecture": "monolith", "message": "ShopDemo monolithique"}

@app.get("/orders")
def orders():
    return {"module": "orders"}

@app.get("/payments")
def payments():
    return {"module": "payments"}

@app.get("/catalog")
def catalog():
    return {"module": "catalog"}
