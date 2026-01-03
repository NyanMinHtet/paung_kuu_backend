from pydantic import BaseModel, EmailStr
from typing import List, Optional

class Skill(BaseModel):
    id: int
    name: str
    description: Optional[str] = None

    class Config:
        from_attributes = True

class User(BaseModel):
    id: int
    email: EmailStr
    bio: Optional[str] = None
    trust_score: float = 0.0
    skills: List[Skill] = []

    class Config:
        from_attributes = True

class UserUpdate(BaseModel):
    bio: Optional[str] = None

class SkillsUpdate(BaseModel):
    skills: List[str]
