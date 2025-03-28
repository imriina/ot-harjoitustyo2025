from entities.user import User
from repository.user_repo import UserRepository
from database_connection import get_database_connection


class DiaryService:
    def __init__(self, user_repo):
        self._user_repo = user_repo
        self._user = None
    
    def create_new_user(self, username, login=True):
        user = self._user_repo.create(User(username))

        if login:
            self._user = user

        return user

diary_service = DiaryService(UserRepository(get_database_connection()))