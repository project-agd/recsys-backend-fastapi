import json

from fastapi.testclient import TestClient

from backend.main import app


def test_client():
    with TestClient(app) as client:
        yield client


class TestIndexViews:
    def test_view(self, client, articles_db):
        payload = {}
        response = client.get(
            url='/',
            data=json.dumps(payload)
        )
