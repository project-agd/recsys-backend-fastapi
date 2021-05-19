from backend import _get_session
from backend.database.models.store import Store


def index():
    session_local = _get_session()
    session_local.query(Store).all()
    return {
        "AllStores": session_local.query(Store).all()
    }
