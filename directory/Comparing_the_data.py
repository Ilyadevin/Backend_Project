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
        self.comparing_ids = self.dictionary['friends_id']
        self.groups_from_dict = self.dictionary['groups']
        self.dictionary_compare = dict

    def find_the_compare(self):
        cur.execute('''SELECT ID_S, INTERESTS, FRIENDS_ID, GROUPS, MUSIC, AGE FROM ID_VK '''
                    )
        data = cur.fetchall()
        dict_of_data = {
            data[0]: {'age': data[5], 'interest': data[1], 'friends': data[2], 'groups': data[3], 'music': data[4]}
        }
        for _ in range(0, 10):
            if self.dictionary['age'] == dict_of_data[data[0]]['age'] or dict_of_data[data[0]]['age'] == -+3:
                good_choice = 200
                regex = re.compile(self.comparing_string)
                we_find = None
                counter_group = 0
                for i in dict_of_data:
                    we_find_group = i['groups']
                    if self.groups_from_dict in we_find_group:
                        counter_group += 1
                    we_find = re.findall(regex, i['interest'])
                counter_music = 0
                for friend in dict_of_data[data[0]]['music']:
                    if friend in self.comparing_ids:
                        counter_music += 1
                    else:
                        pass
                match = 1 * len(we_find) + 1 * counter_music + 1 * counter_group + 1.5 * good_choice
                self.dictionary_compare = {
                    'ids': {'current user': self.dictionary['id'], 'compared_id': dict_of_data.keys()},
                    'compare_status': match}
                for id_vk in dict_of_data:
                    if match >= 100:
                        cur.execute('''SELECT ID_S FROM ID_VK WHERE ID_S=%s''',
                                    (id_vk,))
                        return cur.fetchall()[0]
                    else:
                        pass
            else:
                continue


result = DataCompare()
result.find_the_compare()
