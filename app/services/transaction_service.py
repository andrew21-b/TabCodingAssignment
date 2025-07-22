import json
from pathlib import Path
from app.context.config import settings
from app.schemas.transaction import Transaction

TRANSACTIONS_PATH = Path(settings.TRANSACTIONS_DATA_PATH)

def load_transactions() -> list[Transaction]:
    if not TRANSACTIONS_PATH.exists():
        raise FileNotFoundError(f"Transactions data file not found at {TRANSACTIONS_PATH}")
    
    with open(TRANSACTIONS_PATH, "r") as file:
        data = json.load(file)
        return [Transaction(**item) for item in data]

def get_transactions_by_account(account_id: str) -> list[Transaction]:
    if account_id is None:
        raise ValueError("Account ID must be provided")
    return [transaction for transaction in load_transactions() if str(transaction.accountId) == account_id]
