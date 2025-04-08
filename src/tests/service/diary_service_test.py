import unittest
from service.diary_service import DiaryService
from entities.user import User

class TestDiaryService(unittest.TestCase):
    def setUp(self):
        self.diary_service = DiaryService()
