from pydantic import BaseModel
from datetime import datetime
from enum import Enum
from uuid import UUID

class TransactionType(str, Enum):
    settled = "Settled"
    refunded = "Refunded"
    chargeback = "Chargeback"

class CurrencyType(str, Enum):
    eur = "EUR"
    gbp = "GBP"

class Transaction(BaseModel):
    id: str
    accountId: UUID
    amount: int
    currency: CurrencyType
    type: TransactionType
    dateTime: datetime
