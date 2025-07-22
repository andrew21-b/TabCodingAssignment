from pydantic import BaseModel
from uuid import UUID
from typing import Dict

class Account(BaseModel):
    id: UUID
    name: str

class TransactionSummaryResponse(BaseModel):
    account: Account
    transactions: Dict[str, Dict[str, int]]  # type currencies - amount
    balance: Dict[str, int]