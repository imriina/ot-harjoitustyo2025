from database_connection import get_database_connection
from entities.user import User

class UserRepository:
    def __init__(self, connection):
        self.__connection = connection

    def create(self, user):
        cursor = self.__connection.cursor()
        cursor.execute(
            "INSERT INTO users_table (name) VALUES (?)", (user.username,))
        self.__connection.commit()
        id = cursor.lastrowid
        return (id, user.username)