import unittest

from directory.write_into_SQL import WriteInSQL
from getting_data import WorkWithVk


class TestGettingData(unittest.TestCase):

    def setUp(self) -> None:
        self.log_in = 'Aligruit@gmail.com'
        self.pass_word = '3322879IlyaDevin'

    def test_api(self):
        log_in_class = WorkWithVk(self.log_in, self.pass_word).LogIn()
        self.assertIsInstance(log_in_class, list)
        self.assertEqual(log_in_class[0]['id'], 177107169)


data_test = TestGettingData()
data_test.test_api()


class TestForSQL(unittest.TestCase):
    def setUp(self) -> None:
        self.dictionary = {'id': '177107169',
                           'city': 'Moscow',
                           'name': "Ilya",
                           'bdate': 21,
                           'photo': 'URL',
                           'sex': "Мужской",
                           'interests': "some interest",
                           'friends_id': 'some friends id',
                           'audio': 'some audio',
                           'groups': 'some groups id'}

    def test_SQL(self):
        WriteInSQL().write_in_data_base()


TestForSQL().test_SQL()
