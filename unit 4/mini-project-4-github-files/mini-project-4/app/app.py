from flask import Flask, jsonify, request

app = Flask(__name__)

# Demo-only in-memory records. Do not use real or sensitive student information.
students = [
    {"id": 1, "name": "Aarav Patil", "course": "Computer Science"},
    {"id": 2, "name": "Maya Shah", "course": "Information Technology"},
]
marks = []


@app.get("/api/health")
def health():
    return jsonify({"status": "UP", "service": "student-record-platform"}), 200


@app.get("/api/students")
def get_students():
    return jsonify({"count": len(students), "students": students}), 200


@app.post("/api/marks")
def add_marks():
    payload = request.get_json(silent=True) or {}
    student_id = payload.get("student_id")
    course = payload.get("course")
    score = payload.get("marks")

    if not isinstance(student_id, int) or not course or not isinstance(score, (int, float)):
        return jsonify({
            "error": "Provide integer student_id, course, and numeric marks."
        }), 400
    if score < 0 or score > 100:
        return jsonify({"error": "marks must be between 0 and 100"}), 400
    if not any(student["id"] == student_id for student in students):
        return jsonify({"error": "student_id not found"}), 404

    record = {
        "student_id": student_id,
        "course": str(course),
        "marks": score,
    }
    marks.append(record)
    return jsonify({"message": "Marks recorded for demo", "record": record}), 201


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
