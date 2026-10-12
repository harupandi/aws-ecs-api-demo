from fastapi import APIRouter, HTTPException

router = APIRouter(prefix="/transactions", tags=["transactions"])

@router.get("/")
def list_transactions():
    return []

@router.get("/{transaction_id}")
def get_transaction(transaction_id: int):
    return {"id": transaction_id}