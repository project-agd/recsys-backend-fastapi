import json
import typing
from typing import Optional

from fastapi import FastAPI
from starlette.responses import Response

from .services import store


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


@app.get('/store/{store_id}', response_class=PrettyJSONResponse)
def store_retrieve(store_id: str):
    return store.retrieve(store_id)


@app.get('/items/{item_id}')
def retrieve(item_id: int, q: Optional[str] = None):
    return {'item_id': item_id, 'q': q}
