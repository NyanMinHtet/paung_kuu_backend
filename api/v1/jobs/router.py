from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session
from .schemas import Job, JobCreate
from api.deps import get_db, get_current_user
from models.user import User as UserModel
from crud.job import create_job as crud_create_job, get_active_jobs_by_user_id, get_job_by_id, update_job_status

router = APIRouter()

@router.post("/", response_model=Job)
def create_job(job: JobCreate, db: Session = Depends(get_db), current_user: UserModel = Depends(get_current_user)):
    return crud_create_job(db=db, job=job, learner_id=current_user.id)

@router.get("/active", response_model=List[Job])
def get_active_jobs(db: Session = Depends(get_db), current_user: UserModel = Depends(get_current_user)):
    return get_active_jobs_by_user_id(db=db, user_id=current_user.id)

@router.post("/{job_id}/start", response_model=Job)
def start_job(job_id: int, db: Session = Depends(get_db), current_user: UserModel = Depends(get_current_user)):
    db_job = get_job_by_id(db=db, job_id=job_id)
    if not db_job:
        raise HTTPException(status_code=404, detail="Job not found")
    if current_user.id not in [db_job.learner_id, db_job.mentor_id]:
        raise HTTPException(status_code=403, detail="Not authorized to start this job")
    return update_job_status(db=db, job=db_job, status="started")

@router.post("/{job_id}/complete", response_model=Job)
def complete_job(job_id: int, db: Session = Depends(get_db), current_user: UserModel = Depends(get_current_user)):
    db_job = get_job_by_id(db=db, job_id=job_id)
    if not db_job:
        raise HTTPException(status_code=404, detail="Job not found")
    if current_user.id not in [db_job.learner_id, db_job.mentor_id]:
        raise HTTPException(status_code=403, detail="Not authorized to complete this job")
    return update_job_status(db=db, job=db_job, status="completed")
