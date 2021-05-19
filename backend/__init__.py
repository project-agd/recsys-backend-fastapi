from backend.database.database import SessionLocal


def _get_session():
    return SessionLocal()
