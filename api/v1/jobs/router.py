from fastapi import APIRouter
from typing import List
from .schemas import Job, JobCreate

router = APIRouter()

@router.post("/", response_model=Job)
def create_job(job: JobCreate):
    # In a real app, you'd create a job in the database
    return Job(id=1, task_id=job.task_id, mentor_id=job.mentor_id, learner_id=1, status="booked")

@router.get("/active", response_model=List[Job])
def get_active_jobs():
    # In a real app, you'd fetch active jobs for the current user
    return [
        Job(id=1, task_id=1, mentor_id=2, learner_id=1, status="booked"),
        Job(id=2, task_id=3, mentor_id=4, learner_id=1, status="started"),
    ]

@router.post("/{job_id}/start", response_model=Job)
def start_job(job_id: int):
    # In a real app, you'd update the job status to "started"
    return Job(id=job_id, task_id=1, mentor_id=2, learner_id=1, status="started")

@router.post("/{job_id}/complete", response_model=Job)
def complete_job(job_id: int):
    # In a real app, you'd update the job status to "completed"
    return Job(id=job_id, task_id=1, mentor_id=2, learner_id=1, status="completed")
