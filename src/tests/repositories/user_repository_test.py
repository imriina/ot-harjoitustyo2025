import unittest
from repository.user_repository import user_repository
from entities.user import User

class TestUserRepository(unittest.TestCase):
    def setUp(self):

        user_repository.delete_all()
        self.user_rachel = User('rachel')
        self.user_sabrina = User('sabrina')

    def test_find_by_username(self):

        user_repository.create(self.user_rachel)

        user = user_repository.find_by_username(self.user_rachel.username)

        self.assertEqual(user.username, self.user_rachel.username)

    def test_create(self):
        user_repository.create(self.user_sabrina)
        users = user_repository.find_all()

        self.assertEqual(len(users), 1)
        self.assertEqual(users[0].username, self.user_sabrina.username)

    def test_find_all(self):
        user_repository.create(self.user_rachel)
        user_repository.create(self.user_sabrina)
        users = user_repository.find_all()

        self.assertEqual(len(users), 2)
        self.assertEqual(users[0].username, self.user_rachel.username)
        self.assertEqual(users[1].username, self.user_sabrina.username)
