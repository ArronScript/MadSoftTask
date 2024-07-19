# test_main.py
from fastapi.testclient import TestClient
from .api_main import app

client = TestClient(app)

def test_read_memes():
    response = client.get("/memes/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_read_mem():
    response = client.get("/memes/1")
    assert response.status_code == 200
    assert 'text' in response.json()
    assert 'image_url' in response.json()

def test_create_mem():
    response = client.post("/memes/", json={'text': 'test mem'}, files={'file': ('test.jpg', open('test.jpg', 'rb'), 'image/jpeg')})
    assert response.status_code == 200
    assert 'text' in response.json()
    assert 'image_url' in response.json()

def test_update_mem():
    response = client.put("/memes/1", json={'text': 'updated mem', 'image_url': 'http://localhost:9000/memes/updated.jpg'})
    assert response.status_code == 200
    assert 'text' in response.json()
    assert 'image_url' in response.json()

def test_delete_mem():
    response = client.delete("/memes/1")
    assert response.status_code == 200
    assert response.json() == {'message': 'Mem deleted'}
