from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from api.deps import get_db
from crud.user import create_user, get_user_by_email
from .schemas import UserCreate, UserLogin, Token

router = APIRouter()

@router.post("/register", response_model=UserCreate)
def register(user: UserCreate, db: Session = Depends(get_db)):
    db_user = get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return create_user(db=db, user=user)

@router.post("/login", response_model=Token)
def login(user: UserLogin):
    return Token(access_token="fake-access-token", token_type="bearer")
