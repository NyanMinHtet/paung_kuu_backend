from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from db.base import Base
import datetime

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    wallet_id = Column(Integer, ForeignKey("wallets.id"))
    type = Column(String)  # e.g., "earned", "spent", "escrow_lock", "escrow_release"
    amount = Column(Float)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)

    wallet = relationship("Wallet", back_populates="transactions")
