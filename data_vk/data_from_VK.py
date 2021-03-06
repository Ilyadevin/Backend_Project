import vk_api
from vk_api.audio import VkAudio
import os
import json
import collections
import time

print('Привет! Ты хочешь найти себе пару? '
      'У меня есть кое-что для тебя, но для начала - познакомимся!')
log_in = input("Введите логин: ")
pass_word = input("Введите пароль: ")


def auth_handler():
    print('Если 2-х афторизация не включена [Enter]')
    key = input("Enter authentication code: ")
    remember_device = True
    return key, remember_device


class WorkWithVk:
    def __init__(self, login, password):
        self.login = login
        self.password = password
        self.access_token = 0
        self.audios = []
        self.friends_id = []
        self.groups = []
        self.dictionary = {}
        self.interests = []
        self.VK = None
        self.user_id = None
        self.User = None
        self.User_info = None
        self.User_friends = None
        self.User_groups = None
        self.data = None
        self.city = None
        self.sex = None
        self.photo = None
        self.activities = None
        self.name = None

    def LogIn(self):
        try:
            self.VK = vk_api.VkApi(self.login, self.password, auth_handler=auth_handler)
        except Exception as exception_vk_api:
            print(exception_vk_api)
        time.sleep(2)
        try:
            self.VK.auth()
        except Exception as exception_auth:
            print(exception_auth)
        time.sleep(2)
        VK_auth = self.VK.get_api()

        try:
            self.User = VK_auth.users.get()
            self.User_info = VK_auth.users.get(fields='sex, '
                                                      'city, '
                                                      'interests, '
                                                      'activities, '
                                                      'movies, '
                                                      'photo_400_orig')
            self.User_friends = VK_auth.friends.get()
            self.User_groups = VK_auth.groups.get()
        except Exception as e:
            print(e)

    def detecting_data(self):
        try:
            with open('vk_config.v2.json', 'r') as data_file:
                self.data = json.load(data_file)
            for xxx in self.data[self.login]['token'].keys():
                for yyy in self.data[self.login]['token'][xxx].keys():
                    self.access_token = self.data[self.login]['token'][xxx][yyy]['access_token']
        except Exception as error:
            print(error)

    def check_input(self):
        try:
            for yyy in self.User_info:
                self.city = yyy['city']['title']
                print(f'{self.city} - Ваш город?(Y/N) ')
                decision = input('> ')
                if decision == 'N':
                    breakpoint()
                    self.city = input("Введите правильный город - ")
                else:
                    pass
                self.sex = yyy['sex']
                if self.sex == 1:
                    self.sex = 'Женский'
                elif self.sex == 2:
                    self.sex = 'Мужской'
                elif self.sex == 3:
                    self.sex = "Не указан"
                else:
                    print(TypeError, 'Данные введены не правильно!')
                print(f'Ваш пол - {self.sex}(Y/N)')
                decision = input('> ')
                if decision == 'N':
                    self.sex = input('Введите ваш пол - ')
                else:
                    pass
                self.photo = yyy['photo_400_orig']
                interest = yyy['interests']
                print(f'Ваши интересы(из профиля) - {interest}')
                print('Все данные верны?(Y/N) ')
                decision = input('> ')
                if decision == 'N':
                    interest = input("Чем вы занимаетесь в свободное время? ")
                    self.interests.append(interest.split(' '))
                else:
                    pass
                self.name = self.User[0]['first_name']
                print(f"Вас зовут - {self.name}?(Y/N)")
                decision = input('> ')
                if decision == 'N':
                    self.name = input("Как вас зовут? ")
                else:
                    pass
        except Exception as error_in_input:
            print(error_in_input)
        try:
            for ggg in self.User_groups["items"]:
                self.groups.append(ggg)
            for zzz in self.User_friends["items"]:
                self.friends_id.append(zzz)
            self.user_id = f"https://vk.com/id{self.User[0]['id']}"
        except Exception as error_in_dict:
            print(error_in_dict)
        os.remove('vk_config.v2.json')

    def getting_audios(self):
        vk_audio = VkAudio(self.VK)

        artists = collections.Counter(
            track['artist'] for track in vk_audio.get_iter()
        )
        most_common_artist = artists.most_common(1)[0][0]

        tracks = vk_audio.search(q=most_common_artist, count=10)
        self.audios = []
        for self.n, self.track in enumerate(tracks, 1):
            self.audios.append(self.track['title'])

    def in_dict(self):
        self.dictionary = {'id': self.user_id,
                           'city': self.city,
                           'name': self.name,
                           'photo': self.photo,
                           'sex': self.sex,
                           'interests': self.interests,
                           'friends_id': self.friends_id,
                           'audio': self.audios,
                           'groups': self.groups}
        return self.dictionary


VK_class = WorkWithVk(log_in, pass_word)
VK_class.LogIn()
VK_class.detecting_data()
VK_class.check_input()
VK_class.getting_audios()
dict_data = VK_class.in_dict()
