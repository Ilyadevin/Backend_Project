import unittest

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




