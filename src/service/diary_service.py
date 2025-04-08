from entities.user import User
from repository.user_repository import UserRepository
from database_connection import get_database_connection

from repository.user_repository import (
    user_repository as default_user_repository
)

class InvalidCredentialsError(Exception):
    pass

class DiaryService:
    def __init__(self, user_repository=default_user_repository):
        self._user_repository = user_repository
        self._user = None

    def create_new_user(self, username):
        user = self._user_repository.create(User(username))
        self._user = user
        return user

    def get_logged_in_username(self):
        return self._user.username

    def login(self, username):

        user = self._user_repository.find_by_username(username)
        if not user:
            raise InvalidCredentialsError("Invalid username or password")

        self._user = user
        return user

    def logout(self):
        self._user = None

diary_service = DiaryService()
