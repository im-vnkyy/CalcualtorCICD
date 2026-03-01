from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Calculator API is running!"}

def test_add():
    response = client.get("/add/10/5")
    assert response.status_code == 200
    assert response.json() == {"result": 15}


def test_subtract():
    response = client.get("/subtract/10/5")
    assert response.status_code == 200
    assert response.json() == {"result": 5}


def test_multiply():
    response = client.get("/multiply/10/5")
    assert response.status_code == 200
    assert response.json() == {"result": 50}


def test_divide():
    response = client.get("/divide/10/5")
    assert response.status_code == 200
    assert response.json() == {"result": 2.0}


def test_divide_by_zero():
    response = client.get("/divide/10/0")
    assert response.status_code == 200
    assert response.json() == {"error": "Cannot divide by zero"}