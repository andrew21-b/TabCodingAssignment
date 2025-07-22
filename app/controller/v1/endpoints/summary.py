from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from uuid import UUID
from app.schemas.account import TransactionSummaryResponse
from app.services.summary_service import compute_summary

router = APIRouter()

class SummaryRequest(BaseModel):
    account_id: UUID

@router.post("/summary", response_model=TransactionSummaryResponse)
def get_account_summary(req: SummaryRequest):
    summary = compute_summary(req.account_id)
    if not summary:
        raise HTTPException(status_code=400, detail="Account not found")
    return summary
