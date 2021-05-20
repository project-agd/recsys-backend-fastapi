from backend import _get_session
from backend.db.models.store import Store, StoreCategory, StoreStoreCategoryMap


def retrieve(store_id: str):
    session_local = _get_session()
    result_store = session_local.query(Store).filter(Store.id == store_id).one()
    result_category_map = session_local.query(StoreStoreCategoryMap.store_category_id).filter(
        StoreStoreCategoryMap.store_id == store_id
    ).all()
    result_category_map = (item.store_category_id for item in result_category_map)
    result_category = session_local.query(StoreCategory).filter(
        StoreCategory.id.in_(result_category_map)
    ).all()

    return {
        'result': {
            'store': result_store,
            'category': result_category,
        }
    }
