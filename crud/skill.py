from sqlalchemy.orm import Session
from models.skill import Skill
from models.user import User
from typing import List

def upsert_skills_for_user(db: Session, user: User, skill_names: List[str]) -> List[Skill]:
    # Find existing skills and create new ones for names not found
    existing_skills = db.query(Skill).filter(Skill.name.in_(skill_names)).all()
    existing_skill_names = {skill.name for skill in existing_skills}
    
    new_skills = [
        Skill(name=name) for name in skill_names if name not in existing_skill_names
    ]
    
    # Associate all skills (existing and new) with the user
    user.skills = existing_skills + new_skills
    
    db.add(user)
    db.commit()
    db.refresh(user)
    
    return user.skills
