import importlib.util
from pathlib import Path

APP_PATH = Path(__file__).resolve().parents[1] / "app" / "app.py"
spec = importlib.util.spec_from_file_location("student_app", APP_PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
client = module.app.test_client()


def test_health():
    response = client.get("/api/health")
    assert response.status_code == 200
    assert response.get_json()["status"] == "UP"


def test_students():
    response = client.get("/api/students")
    assert response.status_code == 200
    assert response.get_json()["count"] >= 1


def test_add_marks():
    response = client.post(
        "/api/marks",
        json={"student_id": 1, "course": "Cloud Computing", "marks": 88},
    )
    assert response.status_code == 201


def test_reject_invalid_marks():
    response = client.post(
        "/api/marks",
        json={"student_id": 1, "course": "Cloud Computing", "marks": 120},
    )
    assert response.status_code == 400
