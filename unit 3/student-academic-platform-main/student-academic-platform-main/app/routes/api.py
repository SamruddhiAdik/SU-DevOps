from flask import Blueprint, jsonify, request
from database.db import db
from app.services.academic_service import AcademicService

api = Blueprint("api", __name__)
service = AcademicService(db)


@api.get("/api/health")
def health():
    return jsonify({"status": "healthy"})


@api.get("/api/students")
def get_students():
    return jsonify(db.get_students())


@api.post("/api/students")
def create_student():
    data = request.get_json()

    try:
        student = service.add_student(
            data["student_id"],
            data["name"],
            data["email"]
        )
        return jsonify(student), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400


@api.get("/api/faculty")
def get_faculty():
    return jsonify(db.get_faculty())


@api.get("/api/courses")
def get_courses():
    return jsonify(db.get_courses())


@api.post("/api/courses")
def create_course():
    data = request.get_json()

    try:
        course = service.add_course(
            data["course_id"],
            data["name"],
            int(data["credits"]),
            data["faculty_id"]
        )
        return jsonify(course), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400


@api.post("/api/enrollments")
def create_enrollment():
    data = request.get_json()

    try:
        enrollment = service.enroll_student(
            data["student_id"],
            data["course_id"]
        )
        return jsonify(enrollment), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400


@api.get("/api/enrollments")
def get_enrollments():
    return jsonify(db.get_enrollments())


@api.post("/api/grades")
def create_grade():
    data = request.get_json()

    try:
        grade = service.add_grade(
            data["student_id"],
            data["course_id"],
            data["grade"]
        )
        return jsonify(grade), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400


@api.get("/api/students/<student_id>/gpa")
def get_gpa(student_id):
    try:
        gpa = service.calculate_gpa(student_id)
        return jsonify({
            "student_id": student_id,
            "gpa": gpa
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 400
from database.db import db
from app.services.academic_service import AcademicService

api = Blueprint("api", __name__)
service = AcademicService(db)


@api.get("/api/health")
def health():
    return jsonify({"status": "healthy"})


@api.get("/api/students")
def get_students():
    return jsonify(db.get_students())


@api.post("/api/students")
def create_student():
    data = request.get_json()

    try:
        student = service.add_student(
            data["student_id"],
            data["name"],
            data["email"]
        )
        return jsonify(student), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400


@api.get("/api/faculty")
def get_faculty():
    return jsonify(db.get_faculty())


@api.get("/api/courses")
def get_courses():
    return jsonify(db.get_courses())


@api.post("/api/courses")
def create_course():
    data = request.get_json()

    try:
        course = service.add_course(
            data["course_id"],
            data["name"],
            int(data["credits"]),
            data["faculty_id"]
        )
        return jsonify(course), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400


@api.post("/api/enrollments")
def create_enrollment():
    data = request.get_json()

    try:
        enrollment = service.enroll_student(
            data["student_id"],
            data["course_id"]
        )
        return jsonify(enrollment), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400


@api.get("/api/enrollments")
def get_enrollments():
    return jsonify(db.get_enrollments())


@api.post("/api/grades")
def create_grade():
    data = request.get_json()

    try:
        grade = service.add_grade(
            data["student_id"],
            data["course_id"],
            data["grade"]
        )
        return jsonify(grade), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400


@api.get("/api/students/<student_id>/gpa")
def get_gpa(student_id):
    try:
        gpa = service.calculate_gpa(student_id)
        return jsonify({
            "student_id": student_id,
            "gpa": gpa
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 400
