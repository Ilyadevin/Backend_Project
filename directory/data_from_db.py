import psycopg2
from directory.write_into_SQL import dict_data

connection = psycopg2.connect(
    database="main_data_db",
    user="ilya_erlingas",
    password="3322879",
    host="127.0.0.1",
    port="5432"
)

cur = connection.cursor()


class DataCompare:
    def __init__(self, dictionary):
        self.dictionary_user_data = dictionary
        self.data = None
        self.dict_of_data = {}

    def select_data_from_db(self):
        cur.execute('''SELECT ID_S, INTERESTS, FRIENDS_ID, GROUPS, MUSIC, AGE, PHOTO_LINK FROM ID_VK '''
                    )
        self.data = cur.fetchall()
        self.dict_of_data = {
            self.data[0]: {'id': self.data[0],
                           'age': self.data[5],
                           'interest': self.data[1],
                           'friends': self.data[2],
                           'groups': self.data[3],
                           'music': self.data[4],
                           'photo': self.data[6]}
        }
        return self.dict_of_data


result = DataCompare(dict_data)
data_from_db = result.select_data_from_db()
