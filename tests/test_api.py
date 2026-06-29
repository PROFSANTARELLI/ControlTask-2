import pytest
from fastapi.testclient import TestClient
from backend.main import app
from backend import models, database
=======
from uuid import uuid4

from fastapi.testclient import TestClient
from backend.main import app

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

def create_user_fixture():
    response = client.post(
        "/users",
        json={
            "name": "Usuario Teste",
            "email": f"teste_{uuid4().hex[:8]}@controltask.com",
            "password": "123456"
        }
    )
    assert response.status_code == 201
    return response.json()


def test_create_user():
    response = client.post(
        "/users",
        json={
            "name": "Joao Teste",
            "email": "joao@teste.com",
            "password": "123456"
        }
    )

    assert response.status_code == 201
    assert "id" in response.json()


def test_create_task():
    user = create_user_fixture()

    response = client.post(
        f"/users/{user['id']}/tasks",
        json={
            "title": "Teste Pytest",
            "description": "Executando teste automatizado",
            "priority": "HIGH"
        }
    )

    assert response.status_code == 201
    assert response.json()["title"] == "Teste Pytest"


def test_list_tasks():
    user = create_user_fixture()

    # cria uma tarefa primeiro
    client.post(
        f"/users/{user['id']}/tasks",
        json={
            "title": "Task 1",
            "description": "Lista",
            "priority": "LOW"
        }
    )

    response = client.get(f"/users/{user['id']}/tasks")

    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_update_task():
    user = create_user_fixture()

    task = client.post(
        f"/users/{user['id']}/tasks",
        json={
            "title": "Original",
            "description": "Antes",
            "priority": "LOW"
        }
    ).json()

    task_id = task["id"]

    response = client.put(
        f"/tasks/{task_id}",
        json={
            "title": "Atualizado",
            "description": "Depois",
            "priority": "MEDIUM",
            "status": "COMPLETED"
        }
    )

    assert response.status_code == 200
    assert response.json()["title"] == "Atualizado"
    assert response.json()["status"] == "COMPLETED"


def test_delete_task():
    user = create_user_fixture()

    task = client.post(
        f"/users/{user['id']}/tasks",
        json={
            "title": "Delete me",
            "description": "Para deletar",
            "priority": "LOW"
        }
    ).json()

    task_id = task["id"]

    response = client.delete(f"/tasks/{task_id}")

    assert response.status_code == 204
