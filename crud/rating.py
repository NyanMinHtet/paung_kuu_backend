from sqlalchemy.orm import Session
from models.rating import Rating
from api.v1.ratings.schemas import RatingCreate

def create_rating(db: Session, rating: RatingCreate, rater_id: int) -> Rating:
    db_rating = Rating(
        job_id=rating.job_id,
        rated_user_id=rating.rated_user_id,
        score=rating.score,
        comment=rating.comment,
        rater_id=rater_id,
    )
    db.add(db_rating)
    db.commit()
    db.refresh(db_rating)
    return db_rating

def get_ratings_by_user_id(db: Session, user_id: int) -> list[Rating]:
    return db.query(Rating).filter(Rating.rated_user_id == user_id).all()
