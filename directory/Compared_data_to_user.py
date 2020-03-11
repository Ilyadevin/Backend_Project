import json
import re

from directory.Writting_to_SQL_db import dict_data
from directory.Data_to_compare import data_from_db


class CompareTheData:

    def __init__(self, dictionary, dict_of_data):
        self.whole_match = []
        self.dictionary_user_data = dictionary
        self.dict_of_data = dict_of_data
        self.comparing_string = self.dictionary_user_data['interests']
        self.comparing_ids = self.dictionary_user_data['friends_id']
        self.groups_from_dict = self.dictionary_user_data['groups']
        self.dictionary_compare = dict
        self.match = 0

    def compare_the_data(self):
        try:
            for id_vk in range(0, 10), self.dict_of_data:
                if id_vk == self.dictionary_user_data['id']:
                    continue
                else:
                    if self.dictionary_user_data['age'] == self.dict_of_data.values()['age'] \
                            or self.dict_of_data.values()['age'] == -+3:
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
                        for friend in self.dict_of_data.values()['music']:
                            if friend in self.comparing_ids:
                                counter_music += 1
                            else:
                                pass
                        self.match = 1 * len(we_find) + 1 * counter_music + 1 * counter_group + 1.5 * good_choice
        except Exception as e:
            print(e)

    def getting_similar_data(self):
        if self.match >= 100:
            self.dictionary_compare = {
                'ids': {'current user': self.dictionary_user_data['id'],
                        'photo': self.dict_of_data.values()['photo'],
                        'compared_id': self.dict_of_data.keys()
                        },
                'compare_status': self.match}
            self.whole_match.append(self.match)
        else:
            pass

    def finally_get_it(self):
        sorted(self.whole_match)
        for profile in enumerate(self.whole_match, 10):
            if profile in self.dictionary_compare['compare_status']:
                print(json.dumps(self.dictionary_compare['current user'].values(), indent=1))
            else:
                pass


class_compared = CompareTheData(dictionary=dict_data, dict_of_data=data_from_db)
class_compared.compare_the_data()
class_compared.getting_similar_data()
