from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from api.deps import get_db, get_current_user
from models.user import User as UserModel
from crud.wallet import get_wallet_by_owner_id
from crud.transaction import get_transactions_by_wallet_id
from .schemas import WalletBalance, Transaction
from typing import List

router = APIRouter()

@router.get("/balance", response_model=WalletBalance)
def get_wallet_balance(db: Session = Depends(get_db), current_user: UserModel = Depends(get_current_user)):
    wallet = get_wallet_by_owner_id(db=db, owner_id=current_user.id)
    return wallet

@router.get("/history", response_model=List[Transaction])
def get_wallet_history(db: Session = Depends(get_db), current_user: UserModel = Depends(get_current_user)):
    wallet = get_wallet_by_owner_id(db=db, owner_id=current_user.id)
    return get_transactions_by_wallet_id(db=db, wallet_id=wallet.id)
