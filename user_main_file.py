from getting_data import WorkWithVk

print('Привет! Ты хочешь найти себе пару? '
      'У меня есть кое-что для тебя, но для начала познакомимся!')
log_in = input("Введите логин: ")
pass_word = input("Введите пароль: ")


class UserInterFace(WorkWithVk):

    def __init__(self, login, password):
        super().__init__(login, password, dictionary=self.dictionary)
        self.opposite_sex = None

    def check_input(self, ):
        if self.dictionary['sex'] == 'Мужской':
            self.opposite_sex = 'Женский'
        elif self.dictionary['sex'] == 'Женский':
            self.opposite_sex = 'Мужской'
        else:
            print('Упс, у вас не указаг пол, хотите указать его сейчас?')
            user_input_sex = input('Да / нет?')
            if user_input_sex == 'Да' or 'да':
                user_sex = input('>')
                if user_sex == 'Мужской':
                    self.opposite_sex = 'Женский'
                elif user_sex == 'Женский':
                    self.opposite_sex = 'Мужской'
            if user_input_sex == 'Нет' or 'нет':
                pass
        print("В ващем профиле есть информация, давайте проверим её!")
        print(f'Ваше имя - {self.dictionary["name"]}.\n'
              f'Вам - {self.dictionary["bdate"]}.\n'
              f'Город в котором вы живёте - {self.dictionary["city"]}.\n'
              f'Ваша ссылка на профиль - {self.dictionary["id"]}.\n'
              f'Ваши интересы(указанные в профиле):\n'
              f'{self.dictionary["interests"]}\n')
        decide = input('Верны ли данные?(Y/N)')
        if decide == 'Y':
            pass
        else:
            name = input("Ваше имя? ")
            age = input("Сколько вам лет? ")
            city = input("В каком городе вы живете? ")
            interests = input("Чем вы занимаетесь в свободное время? ")
            new_data = {'name': name, 'bdate': age, 'city': city, 'interests': interests}
            if name and age and city and interests is True:
                self.dictionary.update(new_data)


UserInterFace(log_in, pass_word)
