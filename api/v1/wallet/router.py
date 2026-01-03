from fastapi import APIRouter
from typing import List
from datetime import datetime
from .schemas import WalletBalance, Transaction

router = APIRouter()

@router.get("/balance", response_model=WalletBalance)
def get_wallet_balance():
    # In a real app, you'd fetch the user's wallet balance
    return WalletBalance(available_credits=100.50, locked_credits=25.00)

@router.get("/history", response_model=List[Transaction])
def get_wallet_history():
    # In a real app, you'd fetch the user's transaction history
    return [
        Transaction(id=1, type="earned", amount=50.00, timestamp=datetime.now()),
        Transaction(id=2, type="spent", amount=10.00, timestamp=datetime.now()),
        Transaction(id=3, type="escrow_lock", amount=25.00, timestamp=datetime.now()),
    ]
