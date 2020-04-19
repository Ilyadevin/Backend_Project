import unittest
from working_with_db.writing_to_SQL_db import WriteInSQL
from data_vk.data_from_VK import *
import json


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
        self.dictionary_test = {'id': 'id',
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

    def test_VK_dict(self):
        VK_class.in_dict()
        self.assertEqual(VK_class.in_dict(), dict())

    def test_SQL(self):
        test_SQL_write = WriteInSQL(dictionary_match=self.dictionary_matching_test,
                                    dictionary_profile=self.dictionary_test)
        test_SQL_write.write_matching_status()
        self.assertTrue(test_SQL_write.write_matching_status())
        test_SQL_write.write_profile_in_data_base()
        self.assertTrue(test_SQL_write.write_profile_in_data_base())


TestForSQL().test_SQL()


def setUpModule():
    with open('C:/Users/г/Desktop/WorkSpace/Project_Netology/getting_compared_data/service_data.json', 'r',
              encoding='utf-8') as json_data:
        data = json.load(json_data)
        return data


class TestJsonFile(unittest.TestCase):
    def setUp(self) -> None:
        self.test_data = setUpModule()

    def test_json(self):
        self.assertTrue(self.test_data)
