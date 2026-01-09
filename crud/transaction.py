from sqlalchemy.orm import Session
from models.transaction import Transaction

def get_transactions_by_wallet_id(db: Session, wallet_id: int, skip: int = 0, limit: int = 100) -> list[Transaction]:
    return db.query(Transaction).filter(Transaction.wallet_id == wallet_id).offset(skip).limit(limit).all()
