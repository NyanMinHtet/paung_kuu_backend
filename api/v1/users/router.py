from fastapi import APIRouter
from .schemas import User, UserUpdate, SkillsUpdate, Skill
from typing import List

router = APIRouter()

@router.get("/me", response_model=User)
def get_current_user():
    # In a real app, you'd get the current user from the auth token
    return User(id=1, email="user@example.com", bio="I am a test user.", trust_score=4.5, skills=[Skill(id=1, name="Python", description="I can teach Python.")])

@router.put("/me", response_model=User)
def update_current_user(user_update: UserUpdate):
    # In a real app, you'd update the user in the database
    return User(id=1, email="user@example.com", bio=user_update.bio, trust_score=4.5, skills=[Skill(id=1, name="Python", description="I can teach Python.")])

@router.put("/me/skills", response_model=List[Skill])
def update_user_skills(skills_update: SkillsUpdate):
    # In a real app, you'd update the user's skills in the database
    skills = [Skill(id=i+1, name=skill_name) for i, skill_name in enumerate(skills_update.skills)]
    return skills
