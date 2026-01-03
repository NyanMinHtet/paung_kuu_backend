from pydantic_settings import BaseSettings
import os

class Settings(BaseSettings):
    PROJECT_NAME: str = "Paung Kuu"
    PROJECT_VERSION: str = "1.0.0"

    # Database configuration
    # You should set the DATABASE_URL environment variable.
    # Example for PostgreSQL: DATABASE_URL="postgresql://user:password@host:port/dbname"
    DATABASE_URL: str = "postgresql://postgres:root@localhost/paung_kuu"

    class Config:
        case_sensitive = True
        # This allows loading variables from a .env file
        env_file = ".env"
        env_file_encoding = 'utf-8'

settings = Settings()
