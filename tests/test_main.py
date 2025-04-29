from fastapi.testclient import TestClient
from src.testing_fastapi.main import app

client = TestClient(app)

def test_read_item():
    response = client.get("/items/foo")
    assert response.status_code == 200
    assert response.json() == {"name": "Foo", "description": "A test item"}

def test_read_item_not_found():
    response = client.get("/items/bar")
    assert response.status_code == 404
    assert response.json() == {"detail": "Item not found"}

def test_create_item():
    new_item = {"name": "Bar", "description": "Another test item"}
    response = client.post("/items/bar", json=new_item)
    assert response.status_code == 201
    assert response.json() == new_item

def test_create_item_already_exists():
    new_item = {"name": "Foo", "description": "Duplicate item"}
    response = client.post("/items/foo", json=new_item)
    assert response.status_code == 400
    assert response.json() == {"detail": "Item already exists"}


def test_login_with_correct_password():
    response = client.post("/login?username=user1&password=1234")
    assert response.status_code == 200
    assert response.json()["username"] == "user1"


def test_login_with_wrong_password():
    response = client.post("/login?username=user1&password=123")
    assert response.status_code == 401
    assert response.json() == {"detail": "username or password is incorrect"}