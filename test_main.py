from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_read_news():
    response = client.get("/news")
    assert response.status_code == 200


def test_read_news_search():
    response = client.get("/news?q=bitcoin")
    assert response.status_code == 200
