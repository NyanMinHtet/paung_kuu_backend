from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .schemas import User, UserUpdate, SkillsUpdate, Skill
from typing import List
from api.deps import get_current_user, get_db
from models.user import User as UserModel
from crud.user import update_user
from crud.skill import upsert_skills_for_user

router = APIRouter()

@router.get("/me", response_model=User)
def get_current_user_me(current_user: UserModel = Depends(get_current_user)):
    return current_user

@router.put("/me", response_model=User)
def update_current_user_me(user_update: UserUpdate, db: Session = Depends(get_db), current_user: UserModel = Depends(get_current_user)):
    return update_user(db=db, db_user=current_user, user_in=user_update)

@router.put("/me/skills", response_model=List[Skill])
def update_user_skills(skills_update: SkillsUpdate, db: Session = Depends(get_db), current_user: UserModel = Depends(get_current_user)):
    return upsert_skills_for_user(db=db, user=current_user, skill_names=skills_update.skills)
