from fastapi import FastAPI
from db.session import SessionLocal
from db.init_db import init_db

from api.v1.auth.router import router as auth_router
from api.v1.users.router import router as users_router
from api.v1.tasks.router import router as tasks_router
from api.v1.jobs.router import router as jobs_router
from api.v1.wallet.router import router as wallet_router
from api.v1.ratings.router import router as ratings_router

app = FastAPI(
    # docs_url=True
)

@app.on_event("startup")
def on_startup():
    db = SessionLocal()
    init_db(db)

app.include_router(auth_router, prefix="/api/v1/auth", tags=["auth"])
app.include_router(users_router, prefix="/api/v1/users", tags=["users"])
app.include_router(tasks_router, prefix="/api/v1/tasks", tags=["tasks"])
app.include_router(jobs_router, prefix="/api/v1/jobs", tags=["jobs"])
app.include_router(wallet_router, prefix="/api/v1/wallet", tags=["wallet"])
app.include_router(ratings_router, prefix="/api/v1/ratings", tags=["ratings"])

@app.get("/")
def read_root():
    return {"message": "Welcome to Paung Kuu API"}
