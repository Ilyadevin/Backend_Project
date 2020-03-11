from directory.Data_from_VK import WorkWithVk, dict_data
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
    Tables = None
    if not Tables:
        Tables = cur.execute('''CREATE TABLE ID_VK
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
    else:
        pass


create_db()


class WriteInSQL(WorkWithVk):
    def __init__(self, dictionary, login=None, password=None):
        super().__init__(login, password)
        self.dictionary_new_data = dictionary

    def write_in_data_base(self):
        print("Хотите ли вы чтобы данные вашего профиля были записаны в общую базу данных?(Y/N) ")
        print("Данные используются для статистики и возможного построения выстроения рекламы специально под вас")
        decision = input()
        if decision == 'Y' or 'y':
            name = self.dictionary_new_data['name']
            groups = self.dictionary_new_data['groups']
            sex = self.dictionary_new_data['sex']
            interests = self.dictionary_new_data['interest']
            friends = self.dictionary_new_data['friends_id']
            photo = self.dictionary_new_data['photo']
            city = self.dictionary_new_data['city']
            songs = self.dictionary_new_data['audio']
            user_id_converted = self.dictionary_new_data['id']
            audio = self.dictionary_new_data['audio']
            cur.execute('INSERT INTO ID_VK(LINK,NAME,CITY, PHOTO_LINK, SEX, INTERESTS, SONGS, CITY, FRIENDS_ID, '
                        'GROUPS, '
                        'MUSIC) '
                        'VALUES(%s, %s, %s, %s, %s, %s, %s, %s);',
                        (user_id_converted, name, city, photo, sex, interests, songs, friends, groups, audio,))
            connection.commit()
        elif decision == 'N' or 'n':
            print('Данные не будут записаны в базу')
            pass
        return connection.commit()


SQL = WriteInSQL(dict_data)
SQL.write_in_data_base()
