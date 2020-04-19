import json
from data_vk.data_from_VK import dict_data


class WriteJson:
    def __init__(self, data):
        self.data = data

    def save_in_json(self):
        try:
            with open('../service_data.json', 'a', encoding='utf8') as file:
                templates = json.dump(self.data, file)
            return templates
        except Exception as error:
            print(error)


json_writing = WriteJson(dict_data)
json_data = json_writing.save_in_json()
