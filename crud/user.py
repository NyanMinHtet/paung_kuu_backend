from sqlalchemy.orm import Session
from models.user import User
from api.v1.auth.schemas import UserCreate
from api.v1.users.schemas import UserUpdate
from core.security import get_password_hash

def create_user(db: Session, user: UserCreate) -> User:
    hashed_password = get_password_hash(user.password)
    db_user = User(email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user_by_email(db: Session, email: str) -> User:
    return db.query(User).filter(User.email == email).first()

def update_user(db: Session, db_user: User, user_in: UserUpdate) -> User:
    if user_in.bio is not None:
        db_user.bio = user_in.bio
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
