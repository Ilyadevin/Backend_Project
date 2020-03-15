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
        self.dictionary_matching_test = {
                'ids': {'current user': 1,
                        'photo': 'http//...',
                        'compared_id': 2
                        },
                'compare_status': 101}

    def test_SQL(self):
        test_SQL_write = WriteInSQL(dictionary_match=self.dictionary_matching_test, dictionary_profile=self.dictionary)
        test_SQL_write.write_matching_status()
        self.assertTrue(test_SQL_write.write_matching_status())
        test_SQL_write.write_profile_in_data_base()
        self.assertTrue(test_SQL_write.write_profile_in_data_base())


TestForSQL().test_SQL()
