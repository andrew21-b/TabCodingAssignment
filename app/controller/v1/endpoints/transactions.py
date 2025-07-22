from fastapi import APIRouter
from app.schemas.transaction import Transaction
from app.services.transaction_service import load_transactions, get_transactions_by_account

router = APIRouter()

@router.get("/", response_model=list[Transaction])
def list_transactions():
    return load_transactions()

@router.get("/by-account/{account_id}", response_model=list[Transaction])
def list_transactions_for_account(account_id: str):
    return get_transactions_by_account(account_id)
