from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from db.base import Base

class Job(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True, index=True)
    task_id = Column(Integer, ForeignKey("tasks.id"))
    learner_id = Column(Integer, ForeignKey("users.id"))
    mentor_id = Column(Integer, ForeignKey("users.id"))
    status = Column(String, default="booked")

    task = relationship("Task")
    learner = relationship("User", foreign_keys=[learner_id])
    mentor = relationship("User", foreign_keys=[mentor_id])
