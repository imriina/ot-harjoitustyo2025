import unittest
from repository.post_repository import post_repository
from repository.user_repository import user_repository
from entities.post import Diary
from entities.user import User

class TestPostRepository(unittest.TestCase):
    def setUp(self):
        post_repository.delete_all()
        user_repository.delete_all()

        self.user_milla = User('milla')
        self.user_kaija = User('kaija')
        self.post_a = Diary(post_id=None, username="milla", message="post_a", created_at=None)
        self.post_b = Diary(post_id=None, username="kaija", message="post_b", created_at=None)

        user_repository.create(self.user_milla)
        user_repository.create(self.user_kaija)


    def test_create(self):
        post_repository.create(self.post_a.username, self.post_a.message)
        posts = post_repository.find_all()

        self.assertEqual(len(posts), 1)
        self.assertEqual(posts[0].message, self.post_a.message)
        self.assertEqual(posts[0].username, self.post_a.username)

    def test_find_all(self):
        post_repository.create(self.post_a.username, self.post_a.message)
        post_repository.create(self.post_b.username, self.post_b.message)
        posts = post_repository.find_all()
        self.assertEqual(len(posts), 2)
        self.assertEqual(posts[0].message, self.post_a.message)
        self.assertEqual(posts[1].message, self.post_b.message)

    def test_find_post_by_username(self):
        post_repository.create(self.post_a.username, self.post_a.message)
        post_repository.create(self.post_b.username, self.post_b.message)

        milla_posts = post_repository.find_post_by_username(self.user_milla.username)
        self.assertEqual(len(milla_posts), 1)
        self.assertEqual(milla_posts[0].message, 'post_a')

        kaija_posts = post_repository.find_post_by_username(self.user_kaija.username)
        self.assertEqual(len(kaija_posts), 1)
        self.assertEqual(kaija_posts[0].message, 'post_b')

    def test_delete_post(self):
        post_repository.create(self.post_a.username, self.post_a.message)
        posts = post_repository.find_all()

        self.assertEqual(len(posts), 1)
        post_repository.delete_post(posts[0].post_id)
        posts = post_repository.find_all()

        self.assertEqual(len(posts), 0)