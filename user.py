from abc import ABC, abstractmethod


class User(ABC):
    """Base class that stores account details in a dictionary."""
    def __init__(self, user_id, name, email):
        if not user_id or "@" not in email:
            raise ValueError("A user ID and valid email are required")
        self._data = {"user_id": user_id, "name": name, "email": email}

    @property
    def user_id(self):
        return self._data["user_id"]

    @property
    def email(self):
        return self._data["email"]

    def update_email(self, email):
        if "@" not in email:
            raise ValueError("Please provide a valid email address")
        self._data["email"] = email

    def to_dict(self):
        return self._data.copy()

    @abstractmethod
    def display_profile(self):
        """Return role-specific profile data."""
        raise NotImplementedError
