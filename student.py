from user import User


class Student(User):
    def __init__(self, user_id, name, email):
        super().__init__(user_id, name, email)
        self._data["enrolled_courses"] = []

    def display_profile(self):
        profile = self.to_dict()
        profile["role"] = "Student"
        return profile
