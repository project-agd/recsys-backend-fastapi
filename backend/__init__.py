import sqlalchemy
from sqlalchemy.orm import Session

from backend.db.database import SessionLocal


def _get_session() -> Session:
    return SessionLocal()
