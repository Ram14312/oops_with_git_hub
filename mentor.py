from user import User


class Mentor(User):
    def __init__(self, user_id, name, email, expertise):
        super().__init__(user_id, name, email)
        self._data["expertise"] = expertise

    def display_profile(self):
        profile = self.to_dict()
        profile["role"] = "Mentor"
        return profile
