import pytest

from app import create_app
from database.db import db


@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True

    db.reset()

    with app.test_client() as client:
        yield client

    db.reset()


def test_health(client):
    response = client.get("/api/health")
    assert response.status_code == 200
    assert response.get_json()["status"] == "healthy"


def test_get_students(client):
    response = client.get("/api/students")
    assert response.status_code == 200
    assert len(response.get_json()) == 1


def test_get_courses(client):
    response = client.get("/api/courses")
    assert response.status_code == 200
    assert len(response.get_json()) == 5


def test_successful_enrollment(client):
    response = client.post(
        "/api/enrollments",
        json={"student_id": "S001", "course_id": "CS101"}
    )
    assert response.status_code == 201


def test_duplicate_enrollment(client):
    client.post(
        "/api/enrollments",
        json={"student_id": "S001", "course_id": "CS101"}
    )

    response = client.post(
        "/api/enrollments",
        json={"student_id": "S001", "course_id": "CS101"}
    )

    assert response.status_code == 400


def test_18_credit_limit(client):
    courses = ["CS101", "CS201", "CS301", "CS401"]

    for course_id in courses:
        response = client.post(
            "/api/enrollments",
            json={"student_id": "S001", "course_id": course_id}
        )
        assert response.status_code == 201

    response = client.post(
        "/api/enrollments",
        json={"student_id": "S001", "course_id": "CS404"}
    )

    assert response.status_code == 400


def test_gpa(client):
    client.post(
        "/api/enrollments",
        json={"student_id": "S001", "course_id": "CS101"}
    )
    client.post(
        "/api/enrollments",
        json={"student_id": "S001", "course_id": "CS201"}
    )

    client.post(
        "/api/grades",
        json={
            "student_id": "S001",
            "course_id": "CS101",
            "grade": "A"
        }
    )

    client.post(
        "/api/grades",
        json={
            "student_id": "S001",
            "course_id": "CS201",
            "grade": "B"
        }
    )

    response = client.get("/api/students/S001/gpa")

    assert response.status_code == 200
    assert response.get_json()["gpa"] == 7.86


def test_gpa_api(client):
    client.post(
        "/api/enrollments",
        json={"student_id": "S001", "course_id": "CS101"}
    )

    client.post(
        "/api/grades",
        json={
            "student_id": "S001",
            "course_id": "CS101",
            "grade": "A"
        }
    )

    response = client.get("/api/students/S001/gpa")

    assert response.status_code == 200
    assert "gpa" in response.get_json()
