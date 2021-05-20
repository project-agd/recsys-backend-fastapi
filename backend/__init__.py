import sqlalchemy

from backend.db.database import SessionLocal


def _get_session() -> sqlalchemy.orm.session.Session:
    return SessionLocal()
