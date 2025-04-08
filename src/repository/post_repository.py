from database_connection import get_database_connection
from entities.post import Diary

#def get_user_by_row(row):
#    return User(row["username"]) if row else None

class PostRepository:
    """Käyttäjiin liittyvistä tietokantaoperaatioista vastaava luokka.
    """
    def __init__(self, connection):
        """Luokan konstruktori

        Args:
            connection: Tietokantayhteyden olio
        """
        self._connection = connection

    def create(self, username, message):
        """Tallentaa uuden postauksen käyttäjältä username."""
        cursor = self._connection.cursor()
        cursor.execute(
            "INSERT INTO posts (user_id, message) VALUES (?, ?)",
            (username, message)
        )
        self._connection.commit()

post_repository = PostRepository(get_database_connection())
