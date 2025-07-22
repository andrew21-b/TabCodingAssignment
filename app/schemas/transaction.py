from pydantic import BaseModel

class Transaction(BaseModel):
    id: str
    accountId: str
    amount: str
    currency: str
    type: str
    dateTime: str
