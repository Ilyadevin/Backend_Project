from getting_data import WorkWithVk, log_in, pass_word
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
                 ID_FROM_VK INT NOT NULL,
                 NAME TEXT NOT NULL,
                 SONGS TEXT NOT NULL,
                 CITY TEXT NOT NULL,
                 PHOTO_LINK TEXT NOT NULL,
                 INTERESTS TEXT NOT NULL);
                 ''')
        connection.commit()
    else:
        pass


create_db()


class WriteInSQL(WorkWithVk):
    def __init__(self, login, password):
        super().__init__(login, password, dictionary=self.dictionary)

    def write_in_data_base(self):
        name = self.dictionary['name']
        sex = self.dictionary['sex']
        interests = self.dictionary['interest']
        photo = self.dictionary['photo']
        city = self.dictionary['city']
        songs = self.dictionary['15 первых песен']
        user_id_converted = self.dictionary['id']
        cur.execute('INSERT INTO ID_VK(LINK,NAME,CITY, PHOTO_LINK, SEX, INTERESTS, SONGS, CITY ) VALUES(%s);',
                    (user_id_converted, name, city, photo, sex, interests, songs))
        connection.commit()


SQL = WriteInSQL(log_in, pass_word)
SQL.write_in_data_base()
