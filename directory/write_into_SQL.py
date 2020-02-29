from directory.check_user_data import DataCheck
import psycopg2

connection = psycopg2.connect(
    database="main_data_db",
    user="ilya_erlingas",
    password="3322879",
    host="127.0.0.1",
    port="5432"
)

cur = connection.cursor()


# def create_db():
#     Tables = None
#     if not Tables:
#         Tables = cur.execute('''CREATE TABLE ID_VK
#                  (ID_S SERIAL PRIMARY KEY NOT NULL,
#                  LINK TEXT NOT NULL,
#                  NAME TEXT NOT NULL,
#                  SEX TEXT NOT NULL,
#                  SONGS TEXT NOT NULL,
#                  CITY TEXT NOT NULL,
#                  PHOTO_LINK TEXT NOT NULL,
#                  INTERESTS TEXT NOT NULL,
#                  GROUPS INT NOT NULL,
#                  FRIENDS_ID INT NOT NULL,
#                  MUSIC TEXT NOT NULL);
#                  ''')
#         connection.commit()
#     else:
#         pass
#
#
# create_db()


class WriteInSQL(DataCheck):
    def __init__(self):
        super().__init__()

    def write_in_data_base(self):
        name = self.dictionary['name']
        groups = self.dictionary['groups']
        sex = self.dictionary['sex']
        interests = self.dictionary['interest']
        friends = self.dictionary['friends_id']
        photo = self.dictionary['photo']
        city = self.dictionary['city']
        songs = self.dictionary['audio']
        user_id_converted = self.dictionary['id']
        audio = self.dictionary['audio']
        cur.execute('INSERT INTO ID_VK(LINK,NAME,CITY, PHOTO_LINK, SEX, INTERESTS, SONGS, CITY, FRIENDS_ID, GROUPS, '
                    'MUSIC) '
                    'VALUES(%s, %s, %s, %s, %s, %s, %s, %s);',
                    (user_id_converted, name, city, photo, sex, interests, songs, friends, groups, audio,))
        connection.commit()


SQL = WriteInSQL()
SQL.write_in_data_base()
