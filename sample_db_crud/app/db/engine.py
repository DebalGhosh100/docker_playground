from typing import Generator

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_USERNAME = "debalghosh"

DATABASE_PASSWORD = "debalghosh"

DATABASE_HOST = "postgres-instance"

DATABASE_PORT = "5432"

DATABASE_NAME = "mydatabase"

DATABASE_URL = f"postgresql://{DATABASE_USERNAME}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}"

engine = create_engine(DATABASE_URL, connect_args={})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_session() -> Generator:
    try:
        local_db_connection = SessionLocal()
        yield local_db_connection
    finally:
        local_db_connection.close()
