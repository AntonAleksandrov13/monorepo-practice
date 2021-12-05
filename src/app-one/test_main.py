from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_read():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}


def test_read_items():
    response = client.get("/items/2")
    assert response.status_code == 200
    assert response.json() == {'item_id': 2, 'q': None}


def test_read_items_w_query():
    response = client.get("/items/2?q=somequery")
    assert response.status_code == 200
    assert response.json() == {'item_id': 2, 'q': 'somequery'}
