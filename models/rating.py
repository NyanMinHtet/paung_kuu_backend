from sqlalchemy import Column, Integer, String, ForeignKey, Text
from sqlalchemy.orm import relationship
from db.base import Base

class Rating(Base):
    __tablename__ = "ratings"

    id = Column(Integer, primary_key=True, index=True)
    job_id = Column(Integer, ForeignKey("jobs.id"))
    rater_id = Column(Integer, ForeignKey("users.id"))
    rated_user_id = Column(Integer, ForeignKey("users.id"))
    score = Column(Integer)
    comment = Column(Text, nullable=True)

    job = relationship("Job")
    rater = relationship("User", foreign_keys=[rater_id])
    rated_user = relationship("User", foreign_keys=[rated_user_id])
