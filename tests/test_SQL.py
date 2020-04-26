import unittest
from working_with_db.writing_to_SQL_db import WriteInSQL


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

    def test_SQL(self):
        test_SQL_write = WriteInSQL(dictionary_match=self.dictionary_matching_test,
                                    dictionary_profile=self.dictionary_test)
        test_SQL_write.write_matching_status()
        self.assertTrue(test_SQL_write.write_matching_status())
        test_SQL_write.check_profile_existence()
        self.assertTrue(test_SQL_write.write_profile_in_data_base().user_result, True or False)


if __name__ == '__main__':
    unittest.main()
