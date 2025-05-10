import unittest
from service.diary_service import DiaryService, InvalidCredentialsError
from entities.user import User

class FakeUserRepository:
    def __init__(self):
        self.users =[]

    def create(self, user):
        self.users.append(user)
        return user
    
    def find_all(self):
        return self.users

    def find_by_username(self, username):
        for user in self.users:
            if user.username == username:
                return user
        return None
    
    def delete_all(self):
        self.users = []

class FakePostRepository:
    def __init__(self):
        self.posts = []
        self.id_counter = 1

    def create(self, username, message):
        post = {"id": self.id_counter, "username": username, "message": message}
        self.id_counter += 1
        self.posts.append(post)
        return post
    
    def find_post_by_username(self, username):
        return [post for post in self.posts if post["username"] == username]

    def delete_post(self, post_id):
        self.posts = [post for post in self.posts if post["id"] != post_id]


class TestDiaryService(unittest.TestCase):
    def setUp(self):
        self.user_repository = FakeUserRepository()
        self.post_repository = FakePostRepository()
        self.diary_service = DiaryService(self.user_repository, self.post_repository)

    def create_new_user_(self):
        user = self.diary_service.create_new_user("milla")
        self.assertEqual(user.username, "milla")
        self.assertEqual(self.diary_service.get_logged_in_username(), "milla")

    def test_login_valid_user(self):
        self.user_repository.create(User("milla"))
        user = self.diary_service.login("milla")
        self.assertEqual(user.username, "milla")
    
    def test_login_invalid_user(self):
        with self.assertRaises(InvalidCredentialsError):
            self.diary_service.login("Virheellinen käyttäjänimi")

    def test_create_and_get_posts(self):
        self.diary_service.create_new_user("milla")
        self.diary_service.create_post("post_a")
        self.diary_service.create_post("post_b")

        posts = self.diary_service.get_posts()
        self.assertEqual(len(posts), 2)
        self.assertEqual(posts[0]["message"], "post_a")

    def test_delete_post(self):
        self.diary_service.create_new_user("milla")
        post = self.post_repository.create("milla", "post_a")
        self.diary_service.delete_post(post["id"])

        posts = self.diary_service.get_posts()
        self.assertEqual(len(posts), 0)
        