from database_connection import get_database_connection
from entities.user import User

def get_user_by_row(row):
    return User(row["username"]) if row else None

class UserRepository:
    def __init__(self, connection):
        self._connection = connection

    def create(self, user):

        cursor = self._connection.cursor()

        cursor.execute(
            "insert into users (username) values (?)",
            (user.username,)
        )

        self._connection.commit()

        return user

    def find_by_username(self, username):
        cursor = self._connection.cursor()

        cursor.execute(
            "select * from users where username = ?",
            (username,)
        )

        row = cursor.fetchone()

        return get_user_by_row(row)
        

user_repository = UserRepository(get_database_connection())