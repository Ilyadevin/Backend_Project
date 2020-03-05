import json

from directory.getting_compared_data import similar_data_users
import psycopg2

connection = psycopg2.connect(
    database="main_data_db",
    user="ilya_erlingas",
    password="3322879",
    host="127.0.0.1",
    port="5432"
)

cur = connection.cursor()


class GettingSimilarUsers:
    def __init__(self, data):
        self.similar_data = data

    def finally_get_it(self):
        try:
            for id_vk in self.similar_data:
                cur.execute('''SELECT ID_S, PHOTO_LINK FROM ID_VK WHERE ID_S=%s''',
                            (id_vk['current user'],))
                for row in cur.fetchall()[0]:
                    print(json.dumps(row, indent=1))
        except Exception as e:
            print(e)


wanted_data = GettingSimilarUsers(data=similar_data_users)
wanted_data.finally_get_it()
# We got it!
