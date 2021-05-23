from sqlalchemy.orm import Session

from backend import _get_session
from backend.db.models.store import Store
from backend.db.models.visit_log import VisitLog

from scipy.sparse.linalg import svds
import pandas as pd
import numpy as np


def retrieve_by_user(user_id: int):
    session_local = _get_session()
    stores = session_local.query(Store).all()
    visit_logs = session_local.query(VisitLog).all()

    store_list = list()
    for i in range(len(stores)):
        store_list.append([stores[i].id, stores[i].rating])
    visit_log_list = []
    for i in range(len(visit_logs)):
        visit_log_list.append([visit_logs[i].user_id, visit_logs[i].store_id, visit_logs[i].rating])

    df_ratings = pd.DataFrame(visit_log_list, columns=['userId', 'storeId', 'rating'])
    df_stores = pd.DataFrame(store_list, columns=['storeId', 'rating'])

    df_ratings.drop_duplicates(['userId', 'storeId'], inplace=True, keep='first')

    df_user_store_ratings = df_ratings.pivot(index='userId', columns='storeId', values='rating').fillna(0)
    user_store_ratings = np.array(df_user_store_ratings)
    user_ratings_mean = np.mean(user_store_ratings, axis=1)
    matrix_user_mean = user_store_ratings - user_ratings_mean.reshape(-1,1)

    u, sigma, vt = svds(matrix_user_mean, k=12)

    sigma = np.diag(sigma)
    svd_user_predicted_ratings = np.dot(np.dot(u, sigma), vt) + user_ratings_mean.reshape(-1,1)

    df_svd_preds = pd.DataFrame(svd_user_predicted_ratings, columns=df_user_store_ratings.columns)

    user_row_number = user_id -1

    sorted_user_predictions = df_svd_preds.iloc[user_row_number].sort_values(ascending=False)

    user_data = df_ratings[df_ratings.userId == user_id]
    user_data = user_data.drop(columns=['rating'])
    user_history= user_data.merge(df_stores, on='storeId')
    user_history = user_history.sort_values(by='rating', ascending=False)
    recommendations = df_stores[~df_stores['storeId'].isin(user_history['storeId'])]
    recommendations = recommendations.merge(pd.DataFrame(sorted_user_predictions).reset_index(), on='storeId')
    recommendations = recommendations.rename(columns={user_row_number: 'Predictions'}).sort_values('Predictions', ascending=False).iloc[:10, :]

    recommendations = recommendations['storeId']
    recommendations = list(recommendations)

    return {
        'result': {
            'userid': user_id,
            'recommendations': recommendations,
        }
    }