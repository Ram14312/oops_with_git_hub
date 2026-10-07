from course import *
from student import *
from mentor import *
from enrollment import *


def main():
    # Key each record by its ID. This is the important change from list scanning.
    students = {}
    mentors = {}
    courses = {}

    student = Student("S01", "Ravi Kumar", "ravi@example.com")
    mentor = Mentor("M01", "Asha Rao", "asha@example.com", "Python")
    course = Course("C01", "Python OOP", "OOP fundamentals", "4 weeks", 49, "M01", 2)

    students[student.user_id] = student.to_dict()
    mentors[mentor.user_id] = mentor.display_profile()
    courses[course.course_id] = course.to_dict()

    enrollment = Enrollment.create("E01", "S01", "C01", students, courses)
    print("Enrollment created:", enrollment is not None)
    print("Student record:", students["S01"])
    print("Course record:", courses["C01"])

    enrollment.update_progress(50)
    print("Progress:", enrollment.data["progress"])
    print("Course details:", course.get_course_details(students, mentors))


if __name__ == "__main__":
    main()
