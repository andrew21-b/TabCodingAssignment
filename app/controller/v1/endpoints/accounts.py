from fastapi import APIRouter, HTTPException
from app.schemas.account import Account
from app.services.account_service import load_accounts, get_account_by_id

router = APIRouter()

@router.get("/", response_model=list[Account])
def list_accounts():
    return load_accounts()

@router.get("/{account_id}", response_model=Account)
def read_account(account_id: str):
    account = get_account_by_id(account_id)
    if not account:
        raise HTTPException(status_code=400, detail="Account not found")
    return account
