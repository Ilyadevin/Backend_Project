import json
from directory.Data_from_VK import dict_data

class WriteJson:
    def __init__(self, data):
        self.data = data

    def save_in_json(self):
        with open('service_data.json', 'a', encoding='utf8') as file:
            templates = json.dump(self.data, file)
        return templates


json_writting = WriteJson(dict_data)
json_data = json_writting.save_in_json()
