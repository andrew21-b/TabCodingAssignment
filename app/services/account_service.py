import json
from pathlib import Path
from app.context.config import settings
from app.schemas.account import Account

ACCOUNTS_PATH = Path(settings.ACCOUNTS_DATA_PATH)

def load_accounts():
    if not ACCOUNTS_PATH.exists():
        raise FileNotFoundError(f"Accounts data file not found at {ACCOUNTS_PATH}")
    
    with open(ACCOUNTS_PATH, 'r') as file:
        data = json.load(file)
        return [Account(**item) for item in data]
    
def get_account_by_id(account_id: str) -> Account | ValueError:
    accounts = load_accounts()
    for account in accounts:
        if str(account.id) == account_id:
            return account
    raise ValueError(f"Account with ID {account_id} not found")