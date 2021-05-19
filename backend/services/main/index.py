from backend import _get_session
from backend.db.models.store import Store


async def index():
    session_local = _get_session()
    session_local.query(Store).all()
    return {
        "AllStores": session_local.query(Store).all()
    }
