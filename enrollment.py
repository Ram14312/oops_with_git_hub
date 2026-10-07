from datetime import date


class Enrollment:
    """Static operations use ID-keyed dictionaries supplied by the caller."""
    STATUSES = {"Active", "Completed", "Dropped"}

    def __init__(self, enrollment_id, student_id, course_id):
        self._data = {"enrollment_id": enrollment_id, "student_id": student_id,
                      "course_id": course_id, "enrollment_date": date.today().isoformat(),
                      "status": "Active", "progress": 0}

    @property
    def data(self):
        return self._data.copy()

    @staticmethod
    def create(enrollment_id, student_id, course_id, students_by_id, courses_by_id):
        """Fetch each record by ID; no scan through dictionary key/value pairs."""
        student = students_by_id.get(student_id)
        course = courses_by_id.get(course_id)
        if student is None or course is None:
            return None
        if course_id in student["enrolled_courses"]:
            return None
        if len(course["students"]) >= course["capacity"]:
            return None
        enrollment = Enrollment(enrollment_id, student_id, course_id)
        student["enrolled_courses"].append(course_id)
        course["students"].append(student_id)
        return enrollment

    def cancel_enrollment(self, students_by_id, courses_by_id):
        student = students_by_id.get(self._data["student_id"])
        course = courses_by_id.get(self._data["course_id"])
        if self._data["status"] != "Active" or student is None or course is None:
            return False
        course_id, student_id = self._data["course_id"], self._data["student_id"]
        if course_id not in student["enrolled_courses"] or student_id not in course["students"]:
            return False
        student["enrolled_courses"].remove(course_id)
        course["students"].remove(student_id)
        self._data["status"] = "Dropped"
        return True

    def update_progress(self, progress):
        if self._data["status"] != "Active" or not isinstance(progress, (int, float)) or not 0 <= progress <= 100:
            return False
        self._data["progress"] = progress
        if progress == 100:
            self._data["status"] = "Completed"
        return True

    def complete_course(self):
        return self.update_progress(100)
