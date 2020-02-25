import unittest

from mock import patch

from getting_data import WorkWithVk


class TestGettingData(unittest.TestCase):

    def setUp(self) -> None:
        self.log_in = 'Aligruit@gmail.com'
        self.pass_word = '3322879IlyaDevin'

    def test_api(self, vk):
        api = vk.get_api()
        user_info = api.users.get()
        assert isinstance(user_info, list)
        assert user_info[0]['id'] == 1

    def test_login(self):
        with patch('getting_data.WorkWithVk') as _:
            testing = WorkWithVk('Aligruit@gmail.com', '3322879IlyaDevin')
            testing.LogIn()


data_test = TestGettingData()
data_test.test_login()
