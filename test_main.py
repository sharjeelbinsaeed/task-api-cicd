from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_create_task():
    response = client.post("/tasks", json={"title": "Write tests"})
    assert response.status_code == 201
    body = response.json()
    assert body["title"] == "Write tests"
    assert body["done"] is False


def test_get_tasks_grows():
    before = len(client.get("/tasks").json())
    client.post("/tasks", json={"title": "Buy milk"})
    after = client.get("/tasks").json()
    assert isinstance(after, list)
    assert len(after) == before + 1
    assert any(t["title"] == "Buy milk" for t in after)


def test_create_task_empty_title_fails():
    response = client.post("/tasks", json={"title": "   "})
    assert response.status_code == 400
