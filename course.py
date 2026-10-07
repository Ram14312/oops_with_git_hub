class Course:
    """Course fields and student IDs are stored in a dictionary."""
    def __init__(self, course_id, course_name, description, duration, price,
                 mentor_id=None, capacity=30):
        if not course_id or capacity < 1 or price < 0:
            raise ValueError("Course ID, positive capacity, and nonnegative price are required")
        self._data = {"course_id": course_id, "course_name": course_name,
                      "description": description, "duration": duration,
                      "price": price, "mentor_id": mentor_id,
                      "capacity": capacity, "students": []}

    @property
    def course_id(self):
        return self._data["course_id"]

    def to_dict(self):
        return self._data.copy()

    def display_course(self):
        return self.to_dict()

    def is_available(self):
        return len(self._data["students"]) < self._data["capacity"]

    def add_student(self, student, students_by_id):
        """Find by dictionary key, then add matching IDs to each record once."""
        student_record = student.to_dict() if hasattr(student, "to_dict") else student
        stored_student = students_by_id.get(student_record["user_id"])
        if stored_student is None:
            return False
        if self.course_id in stored_student["enrolled_courses"]:
            return False
        if not self.is_available():
            return False
        stored_student["enrolled_courses"].append(self.course_id)
        self._data["students"].append(stored_student["user_id"])
        return True

    def remove_student(self, student_id, students_by_id):
        """Use ID lookups and remove both sides of the course/student link."""
        student = students_by_id.get(student_id)
        if student is None or student_id not in self._data["students"]:
            return False
        self._data["students"].remove(student_id)
        student["enrolled_courses"].remove(self.course_id)
        return True

    def assign_mentor(self, mentor_id):
        self._data["mentor_id"] = mentor_id

    def update_price(self, new_price):
        if not self.valid_price(new_price):
            raise ValueError("Course price must be a nonnegative number")
        self._data["price"] = new_price

    def get_course_details(self, students_by_id=None, mentors_by_id=None):
        details = self.to_dict()
        if students_by_id is not None:
            details["students"] = [students_by_id[sid] for sid in self._data["students"]]
        if mentors_by_id is not None:
            details["mentor"] = mentors_by_id.get(self._data["mentor_id"])
        return details

    @classmethod
    def create_free_course(cls, course_id, course_name, description, duration,
                           mentor_id=None, capacity=30):
        return cls(course_id, course_name, description, duration, 0, mentor_id, capacity)

    @staticmethod
    def valid_price(price):
        return isinstance(price, (int, float)) and price >= 0
