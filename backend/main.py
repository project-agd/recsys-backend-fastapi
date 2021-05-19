from typing import Optional

from fastapi import FastAPI

from backend.database.database import SessionLocal
from backend.database.models.store import Store

app = FastAPI()


@app.get("/")
def read_root():

    session_local = SessionLocal()
    session_local.query(Store).all()
    return {
        "Hello": "World",
        "Queries": session_local.query(Store).all()
    }


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}
