from database_connection import get_database_connection
from entities.user import User

def get_user_by_row(row):
    return User(row["username"]) if row else None

class UserRepository:
    """Käyttäjiin liittyvistä tietokantaoperaatioista vastaava luokka.
    """

    def __init__(self, connection):
        """Luokan konstruktori

        Args:
            connection: Tietokantayhteyden olio
        """
        self._connection = connection

    def create(self, user):
        """Luo käyttäjän tietokantaan

        Args:
            user: Tallennettava uusi käyttäjä User-oliona

        Returns:
            Tallennettu uusi käyttäjä User-oliona
        """
        cursor = self._connection.cursor()

        cursor.execute(
            "insert into users (username) values (?)",
            (user.username,)
        )

        self._connection.commit()

        return user

    def find_all(self):
        """Palauttaa kaikki käyttäjät

        Returns:
            Lista kaik
            Lista kaikista User-olioistaista User-olioista
        """
        cursor = self._connection.cursor()

        cursor.execute(
            "select * from users"
        )

        rows = cursor.fetchall()

        return list(map(get_user_by_row, rows))

    def find_by_username(self, username):
        """Löytää käyttäjän tietokannasta käyttäjänimellä

        Args:
            username: Etsittävän käyttäjänimi

        Returns:
            Palauttaa User-olion jolla on vastaava käyttäjänimi
        """
        cursor = self._connection.cursor()

        cursor.execute(
            "select * from users where username = ?",
            (username,)
        )

        row = cursor.fetchone()

        return get_user_by_row(row)

    def delete_all(self):
        """Poistaa kaikki käyttäjät.
        """
        cursor = self._connection.cursor()

        cursor.execute("delete from users")

        self._connection.commit()


user_repository = UserRepository(get_database_connection())
