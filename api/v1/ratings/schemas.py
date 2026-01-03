from pydantic import BaseModel
from typing import Optional

class RatingCreate(BaseModel):
    job_id: int
    rated_user_id: int
    score: int # e.g., 1-5
    comment: Optional[str] = None

class Rating(RatingCreate):
    id: int
    rater_id: int

    class Config:
        from_attributes = True
