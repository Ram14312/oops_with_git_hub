# Course Management System

A beginner-friendly Course Management System demonstrating Python object-oriented programming. The root package follows the original dictionary-and-list workflow for looking up students and courses by ID. The `improved_version/` folder provides a second, more object-oriented design for comparison.

## Features

- Create users, students, mentors, courses, and enrollments.
- Enroll and remove students, check capacity, assign mentors, and adjust course prices.
- Track active, completed, and dropped enrollments with progress from 0 to 100.
- Create free courses and display role-specific profiles.
- Prevent duplicate enrollments and reject over-capacity enrollment.
- No third-party dependencies; data is kept in memory.

## Architecture and OOP concepts

| Class | Responsibility |
| --- | --- |
| `User` | Shared ID, name, email, profile display, and email update. |
| `Student(User)` | Student profile and enrolled course tracking. |
| `Mentor(User)` | Mentor profile and area of expertise. |
| `Course` | Course information, mentor, capacity, students, and course operations. |
| `Enrollment` | Connects a student and course; records date, status, and progress. |

The original package demonstrates inheritance (`Student` and `Mentor` extend `User`), encapsulation (student course list is exposed as a copy), and polymorphism (`display_profile` returns role-specific details). `Enrollment` uses a static helper to read dictionary or object fields; `Course.create_free_course` is a class method. `improved_version.models.User` is an abstract base class with an abstract profile method, making abstraction explicit. Its `Course.format_price` is a static method and `Course.free_course` is a class method.

## Installation

Requires Python 3.10 or later. Clone or download this project, then run commands from the project root:

```bash
python --version
python main.py
```

No package installation is required.

## Usage: dictionary-oriented version

```python
from oops_with_github import Course, Enrollment, Mentor, Student

mentor = Mentor("M01", "Asha Rao", "asha@example.com", "Python")
student = Student("S01", "Ravi Kumar", "ravi@example.com")
course = Course("C01", "Python OOP", "OOP basics", "4 weeks", 49, mentor, capacity=20)

# Convert to the dictionary records used in the starter's list-based workflow.
students = [student.display_profile()]
courses = [course.display_course()]
enrollment = Enrollment(students[0], courses[0], "E01")
if enrollment.enroll("S01", "C01", students, courses):
    print("Enrollment successful")
print(students[0]["enrolled_courses"])
print(courses[0]["students"])
```

Run the complete example with `python main.py`.

## Usage: improved object-oriented version

```python
from improved_version import Course, Mentor, Student

mentor = Mentor("M01", "Asha Rao", "asha@example.com", "Python")
student = Student("S01", "Ravi Kumar", "ravi@example.com")
course = Course.free_course("C01", "Python OOP", "OOP basics", "4 weeks", mentor)
enrollment = course.add_student(student)
enrollment.update_progress(60)
print(student.display_profile())
print(Course.format_price(course.price))
```

The improved version is an in-memory teaching example, not persistent storage. It uses direct object references so changes are naturally shared between a student, course, and enrollment.

## Git workflow

Use a feature branch for each change, make focused commits, then merge the reviewed branch. A pull request requires a Git hosting remote (for example, GitHub) and a published feature branch; add your remote and open the PR through your Git host.
