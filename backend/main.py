import json
import typing
from typing import Optional

from fastapi import FastAPI
from starlette.responses import Response

from .services import store, collaborative_filtering, content_based_filtering


class PrettyJSONResponse(Response):
    media_type = "application/json"

    def render(self, content: typing.Any) -> bytes:
        return json.dumps(
            content,
            ensure_ascii=False,
            allow_nan=False,
            indent=4,
            separators=(", ", ": "),
        ).encode("utf-8")


app = FastAPI()


@app.get('/v0/store/{store_id}', response_class=PrettyJSONResponse)
def store_retrieve(store_id: str):
    return store.retrieve(store_id)


@app.get('/recommender/users/{user_id}', response_class=PrettyJSONResponse)
def cf_retrieve(user_id: int):
    return collaborative_filtering.retrieve_by_user(user_id)


@app.get('/recommender/stores/{store_id}', response_class=PrettyJSONResponse)
def cb_retrieve(store_id: str):
    return content_based_filtering.retrieve_by_store(store_id)
