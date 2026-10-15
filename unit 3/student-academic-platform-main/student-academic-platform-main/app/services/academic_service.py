GRADE_POINTS = {"A": 9, "B": 7, "C": 5, "D": 3, "F": 0}

class AcademicService:
    def __init__(self, db):
        self.db = db

    def add_student(self, student_id, name, email):
        return self.db.add_student(student_id, name, email)

    def add_faculty(self, faculty_id, name, email):
        return self.db.add_faculty(faculty_id, name, email)

    def add_course(self, course_id, name, credits, faculty_id):
        if credits <= 0:
            raise ValueError("Credits must be greater than 0")
        return self.db.add_course(course_id, name, credits, faculty_id)

    def enroll_student(self, student_id, course_id):
        course = self.db.get_course(course_id)
        if not course:
            raise ValueError("Course not found")
        current_credits = self.db.get_student_credits(student_id)
        if current_credits + course["credits"] > 18:
            raise ValueError("Student cannot exceed 18 credits")
        return self.db.enroll_student(student_id, course_id)

    def add_grade(self, student_id, course_id, grade):
        if grade not in GRADE_POINTS:
            raise ValueError("Invalid grade")
        return self.db.add_grade(student_id, course_id, grade)

    def calculate_gpa(self, student_id):
        grades = self.db.get_student_grades(student_id)
        if not grades:
            return 0.0

        total_points = 0
        total_credits = 0

        for grade in grades:
            points = GRADE_POINTS[grade["grade"]]
            credits = grade["credits"]
            total_points += points * credits
            total_credits += credits

        if total_credits == 0:
            return 0.0

        if total_credits == 0:
            return 0.0

        return round(total_points / total_credits, 2)
