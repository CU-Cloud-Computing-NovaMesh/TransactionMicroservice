from __future__ import annotations

import os
from typing import Dict, List, Optional
from uuid import UUID
from fastapi import FastAPI, HTTPException, Query

from models.wallet import Wallet
from models.cart import CartItem
from models.transaction import Transaction

port = int(os.environ.get("FASTAPIPORT", 8000))

# -----------------------------------------------------------------------------
# In-memory "databases"
# -----------------------------------------------------------------------------
wallets: Dict[UUID, Wallet] = {}
cart_items: Dict[UUID, CartItem] = {}
transactions: Dict[UUID, Transaction] = {}

# -----------------------------------------------------------------------------
# App
# -----------------------------------------------------------------------------
app = FastAPI(
    title="Transactions API",
    description="Demo FastAPI app using Pydantic v2 models for managing Transactions.",
    version="0.1.0",
)

# -----------------------------------------------------------------------------
# Wallet endpoints
# -----------------------------------------------------------------------------
@app.post("/wallets", response_model=Wallet, status_code=201)
def create_wallet(payload: Wallet):
    raise HTTPException(status_code=501, detail="Not implemented")


@app.get("/wallets", response_model=List[Wallet])
def list_wallets(user_id: Optional[UUID] = Query(None, description="Filter by user ID")):
    raise HTTPException(status_code=501, detail="Not implemented")


@app.get("/wallets/{wallet_id}", response_model=Wallet)
def get_wallet(wallet_id: UUID):
    raise HTTPException(status_code=501, detail="Not implemented")


@app.put("/wallets/{wallet_id}", response_model=Wallet)
def update_wallet(wallet_id: UUID, update: Wallet):
    raise HTTPException(status_code=501, detail="Not implemented")


@app.delete("/wallets/{wallet_id}", status_code=204)
def delete_wallet(wallet_id: UUID):
    raise HTTPException(status_code=501, detail="Not implemented")

# -----------------------------------------------------------------------------
# CartItem endpoints
# -----------------------------------------------------------------------------
@app.post("/cart-items", response_model=CartItem, status_code=201)
def create_cart_item(payload: CartItem):
    raise HTTPException(status_code=501, detail="Not implemented")


@app.get("/cart-items", response_model=List[CartItem])
def list_cart_items(user_id: Optional[UUID] = Query(None, description="Filter by user ID")):
    raise HTTPException(status_code=501, detail="Not implemented")


@app.get("/cart-items/{cart_item_id}", response_model=CartItem)
def get_cart_item(cart_item_id: UUID):
    raise HTTPException(status_code=501, detail="Not implemented")


@app.put("/cart-items/{cart_item_id}", response_model=CartItem)
def update_cart_item(cart_item_id: UUID, update: CartItem):
    raise HTTPException(status_code=501, detail="Not implemented")


@app.delete("/cart-items/{cart_item_id}", status_code=204)
def delete_cart_item(cart_item_id: UUID):
    raise HTTPException(status_code=501, detail="Not implemented")

# -----------------------------------------------------------------------------
# Transaction endpoints
# -----------------------------------------------------------------------------
@app.post("/transactions", response_model=Transaction, status_code=201)
def create_transaction(payload: Transaction):
    raise HTTPException(status_code=501, detail="Not implemented")


@app.get("/transactions", response_model=List[Transaction])
def list_transactions(user_id: Optional[UUID] = Query(None, description="Filter by buyer ID")):
    raise HTTPException(status_code=501, detail="Not implemented")


@app.get("/transactions/{transaction_id}", response_model=Transaction)
def get_transaction(transaction_id: UUID):
    raise HTTPException(status_code=501, detail="Not implemented")


@app.put("/transactions/{transaction_id}", response_model=Transaction)
def update_transaction(transaction_id: UUID, update: Transaction):
    raise HTTPException(status_code=501, detail="Not implemented")


@app.delete("/transactions/{transaction_id}", status_code=204)
def delete_transaction(transaction_id: UUID):
    raise HTTPException(status_code=501, detail="Not implemented")

# -----------------------------------------------------------------------------
# Root
# -----------------------------------------------------------------------------
@app.get("/")
def root():
    return {"message": "Welcome to the Transactions API. See /docs for OpenAPI UI."}

# -----------------------------------------------------------------------------
# Entrypoint
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=True)
