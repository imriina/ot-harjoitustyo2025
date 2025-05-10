from database_connection import get_database_connection
from entities.post import Diary

def get_post_by_row(row):
    return Diary(row["post_id"], row["username"], row["message"], row["created_at"]) if row else None

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
            "INSERT INTO posts (username, message) VALUES (?, ?)",
            (username, message)
        )
        self._connection.commit()

    def find_all(self):
        """Palauttaa kaikki postaukset tietokannasta.

        Returns:
            Lista Diary-olioita uusimmasta vanhimpaan
        """
        cursor = self._connection.cursor()

        cursor.execute("SELECT * FROM posts ORDER BY created_at DESC")
        rows = cursor.fetchall()

        return [get_post_by_row(row) for row in rows]

    def find_post_by_username(self, username):
        """Löytää käyttäjän postaukset tietokannasta käyttäjänimellä

        Args:
            username: Käyttäjänimi jonka postaukset etsitään

        Returns:
            Palauttaa Post-oliot jolla on vastaava käyttäjänimi
        """
        cursor = self._connection.cursor()

        cursor.execute(
            "select * from posts where username = ? order by created_at desc",
            (username,)
        )

        rows = cursor.fetchall()

        if not rows:
            return []

        return [get_post_by_row(row) for row in rows]

    def delete_post(self, post_id):
        """Poistaa käyttäjän postauksen tietokannasta sen id:n perusteella

        Args:
            post_id: Postauksen id jota ollaan poistamassa
        """
        cursor = self._connection.cursor()
        cursor.execute(
            "DELETE FROM posts WHERE post_id = ?",
            (post_id,)
        )
        self._connection.commit()

    def delete_all(self):
        """Poistaa kaikki postaukset tietokannasta."""
        cursor = self._connection.cursor()
        cursor.execute("DELETE FROM posts")
        self._connection.commit()


post_repository = PostRepository(get_database_connection())
