from fastapi import APIRouter
from app.controller.v1.endpoints import accounts, summary, transactions

api_router = APIRouter()

api_router.include_router(accounts.router, prefix="/accounts", tags=["Accounts"])
api_router.include_router(summary.router, prefix="/summary", tags=["Summary"])
api_router.include_router(transactions.router, prefix="/transactions", tags=["Transactions"])
