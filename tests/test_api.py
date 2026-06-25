import pytest
from fastapi.testclient import TestClient
from backend.main import app
from backend import models, database

client = TestClient(app)


@pytest.fixture(autouse=True)
def clean_db():
    models.Base.metadata.drop_all(bind=database.engine)
    models.Base.metadata.create_all(bind=database.engine)


def create_user():
    return client.post(
        "/users",
        json={
            "name": "Teste",
            "email": "teste@ci.com",
            "password": "123"
        }
    ).json()


def test_create_user():
    r = client.post("/users", json={
        "name": "A",
        "email": "a@a.com",
        "password": "123"
    })
    assert r.status_code == 201


def test_create_task():
    user = create_user()

    r = client.post(f"/users/{user['id']}/tasks", json={
        "title": "Task",
        "description": "Desc",
        "priority": "HIGH"
    })

    assert r.status_code == 201


def test_list_tasks():
    user = create_user()

    client.post(f"/users/{user['id']}/tasks", json={
        "title": "Task",
        "priority": "LOW"
    })

    r = client.get(f"/users/{user['id']}/tasks")
    assert r.status_code == 200
    assert isinstance(r.json(), list)


def test_update_task():
    user = create_user()

    task = client.post(f"/users/{user['id']}/tasks", json={
        "title": "Old",
        "priority": "LOW"
    }).json()

    r = client.put(f"/tasks/{task['id']}", json={
        "title": "New",
        "status": "COMPLETED"
    })

    assert r.status_code == 200


def test_delete_task():
    user = create_user()

    task = client.post(f"/users/{user['id']}/tasks", json={
        "title": "Delete",
        "priority": "LOW"
    }).json()

    r = client.delete(f"/tasks/{task['id']}")
    assert r.status_code == 204
