import unittest
from directory.Writting_to_SQL_db import WriteInSQL
from directory.Data_from_VK import WorkWithVk


class TestGettingData(unittest.TestCase):

    def setUp(self) -> None:
        self.log_in = 'password'
        self.pass_word = 'login'

    def test_api(self):
        log_in_class = WorkWithVk(self.log_in, self.pass_word).LogIn()
        self.assertIsInstance(log_in_class, list)
        self.assertEqual(log_in_class[0]['id'], 1)


data_test = TestGettingData()
data_test.test_api()


class TestForSQL(unittest.TestCase):
    def setUp(self) -> None:
        self.dictionary = {'id': 'id',
                           'city': 'moscow',
                           'name': "name",
                           'bdate': 21,
                           'photo': 'URL',
                           'sex': "Мужской",
                           'interests': "some interest",
                           'friends_id': 'some friends id',
                           'audio': 'some audio',
                           'groups': 'some groups id'}

    def test_SQL(self):
        WriteInSQL().write_in_data_base


TestForSQL().test_SQL()
