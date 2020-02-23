import psycopg2
from directory.check_user_data import DataCheck
import re

connection = psycopg2.connect(
    database="main_data_db",
    user="ilya_erlingas",
    password="3322879",
    host="127.0.0.1",
    port="5432"
)

cur = connection.cursor()


class DataCompare(DataCheck):
    def __init__(self):
        super().__init__()
        self.comparing_string = self.dictionary['interests']
        self.counter = 0
        self.comparing_ids = self.dictionary['friends_id']

    def find_the_compare(self):
        cur.execute('''SELECT ID_S, INTERESTS, FRIENDS_ID FROM ID_VK '''
                    )
        data = cur.fetchall()
        dict_of_data = {data[0]: {'interest': data[1], 'friends': data[2]}}
        regex = re.compile(self.comparing_string)
        regex_id = re.compile(self.comparing_ids)
        for i in dict_of_data:
            we_find = re.findall(regex, i['interest'])
            we_find_id = re.findall(regex_id, i['friends'])
            match = 1 * len(we_find) + 2 * len(we_find_id)
            if match >= 500:
                cur.execute('''SELECT ID_S, PHOTO_LINK FROM ID_VK WHERE ID_S=%s''',
                            (i,))
                return cur.fetchall()
            else:
                pass


result = DataCompare()
result.find_the_compare()
