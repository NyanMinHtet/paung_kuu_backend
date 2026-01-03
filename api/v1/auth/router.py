from fastapi import APIRouter
from .schemas import UserCreate, UserLogin, Token

router = APIRouter()

@router.post("/register", response_model=UserCreate)
def register(user: UserCreate):
    return user

@router.post("/login", response_model=Token)
def login(user: UserLogin):
    return Token(access_token="fake-access-token", token_type="bearer")
