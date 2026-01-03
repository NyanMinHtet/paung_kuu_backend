from pydantic import BaseModel
from typing import Optional

class JobCreate(BaseModel):
    task_id: int
    mentor_id: int

class Job(JobCreate):
    id: int
    learner_id: int
    status: str # e.g., "booked", "started", "completed"

    class Config:
        from_attributes = True
