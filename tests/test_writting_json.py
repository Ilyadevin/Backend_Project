import unittest
from data_vk.writing_to_json_file import *


def setUpModule():
    with open('C:/Users/г/Desktop/WorkSpace/Project_Netology/getting_compared_data/service_data.json', 'r',
              encoding='utf-8') as json_data:
        data = json.load(json_data)
        return data


class MyTestCase(unittest.TestCase):

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

    def test_VK_dict(self):
        VK_class.in_dict()
        self.assertEqual(VK_class.in_dict(), dict())


if __name__ == '__main__':
    unittest.main()
