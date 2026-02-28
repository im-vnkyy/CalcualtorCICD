from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Calculator API is running!"}

def test_add():
    response = client.get("/add/10/5")
    assert response.json() == {"result": 15}