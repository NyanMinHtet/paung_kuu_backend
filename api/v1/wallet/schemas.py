from pydantic import BaseModel
from datetime import datetime

class WalletBalance(BaseModel):
    available_credits: float
    locked_credits: float

class Transaction(BaseModel):
    id: int
    type: str # e.g., "earned", "spent", "escrow_lock", "escrow_release"
    amount: float
    timestamp: datetime

    class Config:
        from_attributes = True
