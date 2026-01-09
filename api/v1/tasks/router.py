from fastapi import APIRouter, Depends
from typing import List
from sqlalchemy.orm import Session
from .schemas import Task, TaskCreate
from api.deps import get_db, get_current_user
from crud.task import create_task as crud_create_task, get_tasks as crud_get_tasks
from models.user import User as UserModel

router = APIRouter()

@router.post("/", response_model=Task)
def create_task(task: TaskCreate, db: Session = Depends(get_db), current_user: UserModel = Depends(get_current_user)):
    return crud_create_task(db=db, task=task, user_id=current_user.id)

@router.get("/", response_model=List[Task])
def get_tasks(db: Session = Depends(get_db), skip: int = 0, limit: int = 100):
    return crud_get_tasks(db=db, skip=skip, limit=limit)
