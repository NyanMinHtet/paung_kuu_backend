from sqlalchemy.orm import Session

from db import base  # noqa: F401
from db.session import engine

# make sure all SQL Alchemy models are imported (app.db.base) before initializing DB
# otherwise, SQL Alchemy might fail to initialize relationships properly
# for more details: https://github.com/tiangolo/full-stack-fastapi-postgresql/issues/28


def init_db(db: Session) -> None:
    # Tables should be created with Alembic migrations
    # But for this example, we'll create them here
    base.Base.metadata.create_all(bind=engine)
