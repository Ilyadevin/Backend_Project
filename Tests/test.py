import unittest
from mock import patch
from user_main_file import log_in, pass_word
from getting_data import WorkWithVk


class TestGettingData(unittest.TestCase):

    def setUp(self) -> None:
        self.log_in = 'Aligruit@gmail.com'
        self.pass_word = '3322879IlyaDevin'

    def test_login(self):
        with patch('getting_data.WorkWithVk') as _:
            testing = WorkWithVk('Aligruit@gmail.com', '3322879IlyaDevin')
            testing.LogIn()


data_test = TestGettingData()
data_test.test_login()
