from sqlalchemy.orm import Session
from models.task import Task
from api.v1.tasks.schemas import TaskCreate

def create_task(db: Session, task: TaskCreate, user_id: int) -> Task:
    db_task = Task(**task.model_dump(), poster_id=user_id)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

def get_tasks(db: Session, skip: int = 0, limit: int = 100) -> list[Task]:
    return db.query(Task).offset(skip).limit(limit).all()
