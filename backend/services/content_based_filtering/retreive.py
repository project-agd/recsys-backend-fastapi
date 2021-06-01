from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

from backend import _get_session
from backend.db.models.store import StoreStoreCategoryMap, Store


def retrieve_by_store(store_id: str):
    session_local = _get_session()

    all_category_maps = session_local.query(StoreStoreCategoryMap).order_by(StoreStoreCategoryMap.store_id).all()

    data = list()

    for mm in all_category_maps:
        if len(data) == 0:
            data.append({
                'store_id': mm.store_id,
                'store_category_ids': [str(mm.store_category_id)]
            })
        cur = data[-1]
        if cur.get('store_id') == mm.store_id:
            cur['store_category_ids'].append(str(mm.store_category_id))
        else:
            data.append({
                'store_id': mm.store_id,
                'store_category_ids': [str(mm.store_category_id)]
            })

    for idx, dd in enumerate(data):
        data[idx] = {
            'store_id': dd['store_id'],
            'store_category_ids': ' '.join(dd['store_category_ids'])
        }

    data = pd.DataFrame(data, columns=['store_id', 'store_category_ids'])

    count_vector = CountVectorizer(ngram_range=(1, 3))
    count_vector_categories = count_vector.fit_transform(data['store_category_ids'])
    category_cosine_similarity = cosine_similarity(count_vector_categories, count_vector_categories).argsort()[:, ::-1]
    target_store_index = data[data['store_id'] == store_id].index.values

    similar_indexes = category_cosine_similarity[target_store_index, :9].reshape(-1)
    similar_indexes = similar_indexes[similar_indexes != target_store_index]

    similar_stores_indexes = list()
    for ss in similar_indexes:
        similar_stores_indexes.append(int(ss))

    similar_stores = list()
    for ss in similar_stores_indexes:
        dd = data.iloc[ss]
        store = session_local.query(Store).filter(Store.id == dd['store_id']).first()
        dd['details'] = store
        similar_stores.append(dd)

    return {
        'result': {
            'requested_store':  session_local.query(Store).filter(Store.id == store_id).first(),
            'algorithm': 'cb',
            'recommendations': similar_stores
        }
    }
