import threading


class Database:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super(Database, cls).__new__(cls)
                cls._instance._init_db()
            return cls._instance

    def _init_db(self):
        self.students = {}
        self.faculty = {}
        self.courses = {}
        self.enrollments = []
        self.grades = []
        self._seed_data()

    def _seed_data(self):
        self.students["S001"] = {
            "student_id": "S001",
            "name": "Alice Johnson",
            "email": "alice@university.edu"
        }

        self.faculty["F001"] = {
            "faculty_id": "F001",
            "name": "Dr. Robert Smith",
            "department": "Computer Science"
        }

        self.courses["CS101"] = {
            "course_id": "CS101",
            "name": "Introduction to Programming",
            "credits": 3,
            "faculty_id": "F001"
        }

        self.courses["CS201"] = {
            "course_id": "CS201",
            "name": "Data Structures",
            "credits": 4,
            "faculty_id": "F001"
        }

        self.courses["CS301"] = {
            "course_id": "CS301",
            "name": "Cloud Computing",
            "credits": 4,
            "faculty_id": "F001"
        }

        self.courses["CS401"] = {
            "course_id": "CS401",
            "name": "DevOps Engineering",
            "credits": 4,
            "faculty_id": "F001"
        }

        self.courses["CS404"] = {
            "course_id": "CS404",
            "name": "Artificial Intelligence",
            "credits": 4,
            "faculty_id": "F001"
        }

    def get_students(self):
        return list(self.students.values())

    def get_faculty(self):
        return list(self.faculty.values())

    def get_courses(self):
        return list(self.courses.values())

    def get_course(self, course_id):
        return self.courses.get(course_id)

    def add_student(self, student_id, name, email):
        if student_id in self.students:
            raise ValueError("Student already exists")
        student = {"student_id": student_id, "name": name, "email": email}
        self.students[student_id] = student
        return student

    def add_faculty(self, faculty_id, name, email):
        if faculty_id in self.faculty:
            raise ValueError("Faculty already exists")
        faculty = {"faculty_id": faculty_id, "name": name, "email": email}
        self.faculty[faculty_id] = faculty
        return faculty

    def add_course(self, course_id, name, credits, faculty_id):
        if course_id in self.courses:
            raise ValueError("Course already exists")
        course = {"course_id": course_id, "name": name, "credits": credits, "faculty_id": faculty_id}
        self.courses[course_id] = course
        return course

    def get_student_credits(self, student_id):
        return sum(self.courses[e["course_id"]]["credits"] for e in self.enrollments if e["student_id"] == student_id)

    def enroll_student(self, student_id, course_id):
        if any(e["student_id"] == student_id and e["course_id"] == course_id for e in self.enrollments):
            raise ValueError("Student already enrolled")
        enrollment = {"student_id": student_id, "course_id": course_id}
        self.enrollments.append(enrollment)
        return enrollment

    def get_enrollments(self):
        return self.enrollments

    def add_grade(self, student_id, course_id, grade):
        record = {"student_id": student_id, "course_id": course_id, "grade": grade}
        self.grades.append(record)
        return record

    def get_student_grades(self, student_id):
        result = []
        for grade in self.grades:
            if grade["student_id"] == student_id:
                item = dict(grade)
                item["credits"] = self.courses[grade["course_id"]]["credits"]
                result.append(item)
        return result

    def reset(self):
        with self._lock:
            self.students.clear()
            self.faculty.clear()
            self.courses.clear()
            self.enrollments.clear()
            self.grades.clear()
            self._seed_data()


db = Database()
import threading


