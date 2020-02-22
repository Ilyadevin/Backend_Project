import psycopg2
from user_main_file import UserInterFace
import re
connection = psycopg2.connect(
    database="main_data_db",
    user="ilya_erlingas",
    password="3322879",
    host="127.0.0.1",
    port="5432"
)

cur = connection.cursor()


class DataCompare(UserInterFace):
    def __init__(self, login=None, password=None):
        super().__init__(login, password)
        self.comparing_string = self.dictionary['interests']
        self.counter = 0

    def find_the_compare(self):
        cur.execute('''SELECT INTERESTS FROM ID_VK '''
                    )
        interests = cur.fetchall()
        regex = re.compile(self.comparing_string)
        we_find = re.findall(regex, interests)
        if we_find is True:
            cur.execute('''SELECT LINK, PHOTO_LINK FROM ID_VK WHERE INTERESTS=%s''',
                        (we_find,))
            return cur.fetchall()
        else:
            print("No matches, sorry")
