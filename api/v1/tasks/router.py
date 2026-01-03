from fastapi import APIRouter
from typing import List
from .schemas import Task, TaskCreate

router = APIRouter()

@router.post("/", response_model=Task)
def create_task(task: TaskCreate):
    # In a real app, you'd save the task to the database
    return Task(id=1, title=task.title, description=task.description, poster_id=1)

@router.get("/", response_model=List[Task])
def get_tasks():
    # In a real app, you'd fetch tasks from the database
    return [
        Task(id=1, title="Learn Python", description="I want to learn the basics of Python.", poster_id=1),
        Task(id=2, title="Fix a bug", description="I have a bug in my React app.", poster_id=2),
    ]
