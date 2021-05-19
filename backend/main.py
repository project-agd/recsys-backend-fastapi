from typing import Optional

from fastapi import FastAPI

from backend.service import main

app = FastAPI()


@app.get("/")
async def index():
    return await main.index()


@app.get("/items/{item_id}")
def retrieve(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}
