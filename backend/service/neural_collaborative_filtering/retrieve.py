from tensorflow import keras

from backend import _get_session
from backend.database.models.store import Store


def retrieve():
    session_local = _get_session()
    session_local.query(Store).all()
    # keras
