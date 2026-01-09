from sqlalchemy.orm import Session
from models.job import Job
from api.v1.jobs.schemas import JobCreate

def create_job(db: Session, job: JobCreate, learner_id: int) -> Job:
    db_job = Job(
        task_id=job.task_id,
        mentor_id=job.mentor_id,
        learner_id=learner_id,
        status="booked",
    )
    db.add(db_job)
    db.commit()
    db.refresh(db_job)
    return db_job

def get_active_jobs_by_user_id(db: Session, user_id: int) -> list[Job]:
    return db.query(Job).filter(
        ((Job.learner_id == user_id) | (Job.mentor_id == user_id)),
        Job.status != "completed"
    ).all()

def get_job_by_id(db: Session, job_id: int) -> Job | None:
    return db.query(Job).filter(Job.id == job_id).first()

def update_job_status(db: Session, job: Job, status: str) -> Job:
    job.status = status
    db.commit()
    db.refresh(job)
    return job
