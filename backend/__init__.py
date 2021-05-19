from backend.db.database import SessionLocal


def _get_session():
    return SessionLocal()
