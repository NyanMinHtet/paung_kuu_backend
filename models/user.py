from sqlalchemy import Column, Integer, String, Boolean, Float
from sqlalchemy.orm import relationship
from db.base import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    bio = Column(String, nullable=True)
    trust_score = Column(Float, default=0.0)

    skills = relationship("Skill", back_populates="owner")
    tasks = relationship("Task", back_populates="poster")
    wallet = relationship("Wallet", uselist=False, back_populates="owner")
