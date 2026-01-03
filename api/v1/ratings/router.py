from fastapi import APIRouter
from typing import List
from .schemas import Rating, RatingCreate

router = APIRouter()

@router.post("/", response_model=Rating)
def create_rating(rating: RatingCreate):
    # In a real app, you'd save the rating to the database
    return Rating(id=1, rater_id=1, **rating.dict())

@router.get("/user/{user_id}", response_model=List[Rating])
def get_user_ratings(user_id: int):
    # In a real app, you'd fetch ratings for the specified user
    return [
        Rating(id=1, job_id=1, rater_id=1, rated_user_id=user_id, score=5, comment="Great mentor!"),
        Rating(id=2, job_id=2, rater_id=2, rated_user_id=user_id, score=4, comment="Very helpful."),
    ]
