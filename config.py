import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    # Use DATABASE_URL env var for production (e.g. a Postgres URI). Fall back to a local
    # SQLite DB for development so getting started is friction-free.
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///paung_kuu_dev.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
