from sqlalchemy.orm import Session
from models.wallet import Wallet

def get_wallet_by_owner_id(db: Session, owner_id: int) -> Wallet:
    wallet = db.query(Wallet).filter(Wallet.owner_id == owner_id).first()
    if not wallet:
        wallet = Wallet(owner_id=owner_id, available_credits=0.0, locked_credits=0.0)
        db.add(wallet)
        db.commit()
        db.refresh(wallet)
    return wallet
