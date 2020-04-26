import psycopg2

connection = psycopg2.connect(
    database="main_data_db",
    user="ilya_erlingas",
    password="3322879",
    host="127.0.0.1",
    port="5432"
)

cursor = connection.cursor()


def create_db():
    cursor.execute('''CREATE TABLE ID_VK
                 (ID_US SERIAL PRIMARY KEY NOT NULL,
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

    cursor.execute('''CREATE TABLE MATCHING
                (ID SERIAL PRIMARY KEY NOT NULL,
                FIRST_ID TEXT NOT NULL,
                PHOTO_LINK TEXT NOT NULL,
                SECOND_ID TEXT NOT NULL,
                MATCH INT NOT NULL);''')
    cursor.execute('''CREATE TABLE JOINED_TABLE
    (ID SERIAL PRIMARY KEY NOT NULL,
    ID_VK_ONE TEXT REFERENCES ID_VK(ID_US),
    ID_VK_ANOTHER TEXT REFERENCES MATCHING(SECOND_ID),
    MATCHING_STATUS INT REFERENCES MATCHING(MATCH));''')


create_db()


class WriteInSQL:
    def __init__(self, dictionary_profile, dictionary_match):
        self.dictionary_profile = dictionary_profile
        self.dictionary_match = dictionary_match

    def check_profile_existence(self):
        cursor.execute('''SELECT LINK FROM ID_VK WHERE LINK = %s''',
                       (self.dictionary_profile['id']))
        decision = cursor.fetchall()
        if decision is True:
            user_result = True
        elif decision is False:
            user_result = False
        else:
            pass

    def write_matching_status(self):
        cursor.execute('''INSERT INTO MATCHING(FIRST_ID, PHOTO_LINK, SECOND_ID, MATCH INT)'''
                       '''VALUES(%s, %s, %s, %s);''',
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
            cursor.execute('''INSERT INTO ID_VK(LINK,NAME,CITY, PHOTO_LINK, SEX, INTERESTS, SONGS, CITY, FRIENDS_ID, '''
                           '''GROUPS, '''
                           '''MUSIC) '''
                           '''VALUES(%s, %s, %s, %s, %s, %s, %s, %s);''',
                           (user_id_converted, name, city, photo, sex, interests, songs, friends, groups, audio,))
            connection.commit()
        elif decision == 'N':
            print('Данные не будут записаны в базу')
        else:
            print('Error')

        return connection.commit()

    def writing_in_joined_table(self):
        cursor.execute('''INSERT INTO JOINED_TABLE(ID_VK_ONE, ID_VK_ANOTHER, MATCHING_STATUS) VALUES(%s, %s, %s)''',
                       (self.dictionary_match['ids']['current user'], self.dictionary_match['ids']['compared_id'],
                        self.dictionary_match['compare_status'],))
        return connection.commit()

    def joined_table(self):
        cursor.execute('''SELECT ID_VK_ONE, ID_VK_ANOTHER, MATCHING_STATUS
            FROM JOINED_TABLE WHERE ID_VK_ONE=%s''',
                       (self.dictionary_match['ids']['current user'],))
        return cursor.fetchall()
