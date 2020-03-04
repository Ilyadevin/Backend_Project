import json
import psycopg2
from directory.write_into_SQL import dict_data
import re

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
        self.comparing_string = self.dictionary_user_data['interests']
        self.comparing_ids = self.dictionary_user_data['friends_id']
        self.groups_from_dict = self.dictionary_user_data['groups']
        self.dictionary_compare = dict
        self.dict_of_data = {}

    def select_data_from_db(self):
        cur.execute('''SELECT ID_S, INTERESTS, FRIENDS_ID, GROUPS, MUSIC, AGE FROM ID_VK '''
                    )
        self.data = cur.fetchall()
        self.dict_of_data = {
            self.data[0]: {'id': self.data[0],
                           'age': self.data[5],
                           'interest': self.data[1],
                           'friends': self.data[2],
                           'groups': self.data[3],
                           'music': self.data[4]}
        }

    def compare_the_data(self):
        for _ in range(0, 10):
            if self.dictionary_user_data['age'] == self.dict_of_data[self.data[0]]['age'] \
                    or self.dict_of_data[self.data[0]]['age'] == -+3:
                good_choice = 200
                regex = re.compile(self.comparing_string)
                we_find = None
                counter_group = 0
                for i in self.dict_of_data:
                    we_find_group = i['groups']
                    if self.groups_from_dict in we_find_group:
                        counter_group += 1
                    we_find = re.findall(regex, i['interest'])
                counter_music = 0
                for friend in self.dict_of_data[self.data[0]]['music']:
                    if friend in self.comparing_ids:
                        counter_music += 1
                    else:
                        pass
                match = 1 * len(we_find) + 1 * counter_music + 1 * counter_group + 1.5 * good_choice
                self.dictionary_compare = {
                    'ids': {'current user': self.dictionary_user_data['id'],
                            'compared_id': self.dict_of_data.keys()
                            },
                    'compare_status': match}
                for id_vk in self.dict_of_data:
                    if match >= 100:
                        if id_vk == self.dictionary_user_data['id']:
                            continue
                        else:
                            cur.execute('''SELECT ID_S, PHOTO_LINK FROM ID_VK WHERE ID_S=%s''',
                                        (id_vk,))
                            for row in cur.fetchall()[0]:
                                print(json.dumps(row, indent=1))
                    else:
                        pass
            else:
                continue


result = DataCompare(dict_data)
result.select_data_from_db()
result.compare_the_data()
