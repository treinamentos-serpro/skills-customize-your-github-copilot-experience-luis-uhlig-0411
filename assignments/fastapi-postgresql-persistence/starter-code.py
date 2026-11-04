import os
from collections.abc import Generator

from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker

DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise RuntimeError("Set the DATABASE_URL environment variable before starting the API.")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine, autoflush=False, expire_on_commit=False)


class Base(DeclarativeBase):
    pass


app = FastAPI(title="Book Catalog API")


def get_db() -> Generator[Session, None, None]:
    with SessionLocal() as db:
        yield db


@app.get("/health")
def health_check():
    return {"status": "ok"}


# Add the Book model, database tables, request schemas, and CRUD routes in the tasks.
