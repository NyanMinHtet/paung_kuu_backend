from fastapi import APIRouter, Depends
from typing import List
from sqlalchemy.orm import Session
from .schemas import Rating, RatingCreate
from api.deps import get_db
from crud.rating import create_rating as crud_create_rating, get_ratings_by_user_id

router = APIRouter()

@router.post("/", response_model=Rating)
def create_rating(rating: RatingCreate, db: Session = Depends(get_db), current_user: UserModel = Depends(get_current_user)):
    return crud_create_rating(db=db, rating=rating, rater_id=current_user.id)

@router.get("/user/{user_id}", response_model=List[Rating])
def get_user_ratings(user_id: int, db: Session = Depends(get_db)):
    return get_ratings_by_user_id(db=db, user_id=user_id)
