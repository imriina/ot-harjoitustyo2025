from entities.user import User
from repository.user_repository import (
    user_repository as default_user_repository
)
from repository.post_repository import (
    post_repository as default_post_repository
)

class InvalidCredentialsError(Exception):
    pass

class DiaryService:
    """Luokka, joka hoitaa sovelluslogiikkaa
    """
    def __init__(self, user_repository=default_user_repository,
                 post_repository=default_post_repository):
        self._user_repository = user_repository
        self._post_repository = post_repository
        self._user = None

    def create_new_user(self, username):
        """Luo uuden käyttäjän ja kirjautuu sisään

        Args:
            username: merkkijono, käyttäjätunnus

        Returns:
            Uusi käyttäjä User-oliona
        """
        user = self._user_repository.create(User(username))
        self._user = user
        return user

    def get_logged_in_username(self):
        """Palauttaa sisäänkirjautuneen käyttäjänimen

        Returns:
            Kirjautununeen käyttäjänimi User-oliona
        """
        return self._user.username

    def login(self, username):
        """Sisäänkirjautuminen käyttäjänimellä

        Args:
            username: merkkijono, joka on yksilöllinen käyttäjänimi

        Raises:
            InvalidCredentialsError: virhe, jos käyttäjää ei ole

        Returns:
            Kirjautunut käyttäjä User-oliona
        """

        user = self._user_repository.find_by_username(username)
        if not user:
            raise InvalidCredentialsError("Virheellinen käyttäjänimi")

        self._user = user
        return user

    def logout(self):
        """Uloskirjaa sisäänkirjautuneen käyttäjän
        """
        self._user = None

    def create_post(self, message):
        """Kirjaa uuden postauksen

        Args:
            note: merkkijono, kirjattu viesti
        """
        self._post_repository.create(self._user.username, message)

    def get_posts(self):
        """Palauttaa käyttäjän kirjaamat postaukset

        Returns:
            Lista käyttäjän postauksista
        """
        return self._post_repository.find_post_by_username(self._user.username)

    def delete_post(self, post_id):
        """Poistaa käyttäjän tekemän postauksen

        Args:
            post_id: postettavan postauksen id
        """
        self._post_repository.delete_post(post_id)


diary_service = DiaryService()
