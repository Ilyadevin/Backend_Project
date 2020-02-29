from getting_data import WorkWithVk


class DataCheck(WorkWithVk):
    def __init__(self, login=None, password=None):
        super().__init__(login, password)
        self.interest_input = []
        self.opposite_sex = None
        self.new_data = None
        self.age = None
        self.name = None
        self.city = None
        self.interests = None
        self.new_data = {}

    def check_input(self):
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
        if decide == 'Y' or 'y':
            pass
        elif decide == 'N' or 'n':
            self.name = input("Ваше имя? ")
            self.age = input("Сколько вам лет? ")
            self.city = input("В каком городе вы живете? ")
            self.interests = input("Чем вы занимаетесь в свободное время? ")
            for i in self.interests:
                if len(i) > 3:
                    self.interest_input.append(i)
            self.new_data = {'name': self.name,
                             'bdate': self.age,
                             'city': self.city,
                             'interests': self.interest_input}
            return self.new_data
        else:
            print('Error')

    def update_dict(self):
        self.dictionary.update(self.new_data)
        return self.dictionary


dict_final = DataCheck()
dict_final.update_dict()
