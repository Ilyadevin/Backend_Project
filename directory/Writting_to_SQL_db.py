import psycopg2

connection = psycopg2.connect(
    database="main_data_db",
    user="ilya_erlingas",
    password="3322879",
    host="127.0.0.1",
    port="5432"
)

cur = connection.cursor()


def create_db():
    cur.execute('''CREATE TABLE ID_VK
                 (ID_S SERIAL PRIMARY KEY NOT NULL,
                 LINK TEXT NOT NULL,
                 NAME TEXT NOT NULL,
                 SEX TEXT NOT NULL,
                 SONGS TEXT NOT NULL,
                 CITY TEXT NOT NULL,
                 PHOTO_LINK TEXT NOT NULL,
                 INTERESTS TEXT NOT NULL,
                 GROUPS INT NOT NULL,
                 FRIENDS_ID INT NOT NULL,
                 MUSIC TEXT NOT NULL);
                 ''')
    connection.commit()

    cur.execute('''CREATE TABLE MATCHING
                (ID SERIAL PRIMARY KEY NOT NULL,
                FIRST_ID TEXT NOT NULL,
                PHOTO_LINK TEXT NOT NULL,
                SECOND_ID TEXT NOT NULL
                MATCH INT NOT NULL);''')


create_db()


class WriteInSQL:
    def __init__(self, dictionary_profile, dictionary_match):
        self.dictionary_profile = dictionary_profile
        self.dictionary_match = dictionary_match

    def write_matching_status(self):
        cur.execute('INSERT INTO MATCHING(FIRST_ID, PHOTO_LINK, SECOND_ID, MATCH INT)'
                    'VALUES(%s, %s, %s, %s);',
                    (self.dictionary_match['ids']['current user'], self.dictionary_match['ids']['photo'],
                     self.dictionary_match['ids']['compared_id'], self.dictionary_match['compare_status'],))
        connection.commit()

    def write_profile_in_data_base(self):
        print("Хотите ли вы чтобы данные вашего профиля были записаны в общую базу данных?(Y/N) ")
        print("Данные используются для статистики и возможного построения выстроения рекламы специально под вас")
        decision = input()
        if decision == 'Y':
            name = self.dictionary_profile['name']
            groups = self.dictionary_profile['groups']
            sex = self.dictionary_profile['sex']
            interests = self.dictionary_profile['interest']
            friends = self.dictionary_profile['friends_id']
            photo = self.dictionary_profile['photo']
            city = self.dictionary_profile['city']
            songs = self.dictionary_profile['audio']
            user_id_converted = self.dictionary_profile['id']
            audio = self.dictionary_profile['audio']
            cur.execute('INSERT INTO ID_VK(LINK,NAME,CITY, PHOTO_LINK, SEX, INTERESTS, SONGS, CITY, FRIENDS_ID, '
                        'GROUPS, '
                        'MUSIC) '
                        'VALUES(%s, %s, %s, %s, %s, %s, %s, %s);',
                        (user_id_converted, name, city, photo, sex, interests, songs, friends, groups, audio,))
            connection.commit()
        elif decision == 'N':
            print('Данные не будут записаны в базу')
        else:
            print('Error')

        return connection.commit()
