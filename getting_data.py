import vk
import vk_api
from vk_api.audio import VkAudio
import os
import json
import collections

#
log_in = input("Введите логин: ")
#
pass_word = input("Введите пароль: ")


def auth_handler():
    key = input("Enter authentication code: ")
    remember_device = True
    return key, remember_device


class WorkWithVk:
    def __init__(self, login, password, VK=None, user_id=None, access_token=0, dictionary=None, track=None):
        if dictionary is None:
            dictionary = {}
        self.login = login
        self.password = password
        self.VK = VK
        self.user_id = user_id
        self.access_token = access_token
        self.dictionary = dictionary
        self.track = track

    def LogIn(self):
        self.VK = vk_api.VkApi(self.login, self.password, auth_handler=auth_handler)
        self.VK.auth()
        VK_auth = self.VK.get_api()

        try:
            User = VK_auth.users.get()
            User_2 = VK_auth.users.get(fields='sex, city, interests, activities, music, movies, photo_400_orig')
            print(User_2)
        except Exception as e:
            print(e)
        else:
            print(f"\nHello {User[0]['first_name']}")

            with open('vk_config.v2.json', 'r') as data_file:
                data = json.load(data_file)

            for xxx in data[self.login]['token'].keys():
                for yyy in data[self.login]['token'][xxx].keys():
                    self.access_token = data[self.login]['token'][xxx][yyy]['access_token']

            print('=' * 85)
            print(f"Твой ID {User[0]['id']}")
            self.user_id = User[0]['id']
            print('=' * 85)
            print(f"Access_Token: {self.access_token}")
            print('=' * 85)
            os.remove('vk_config.v2.json')

    def getting_15_audios(self):
        vk_audio = VkAudio(self.VK)

        artists = collections.Counter(
            track['artist'] for track in vk_audio.get_iter()
        )
        print('Top 15:')
        for artist, tracks in artists.most_common(15):
            print('{} - {} tracks'.format(artist, tracks))
        most_common_artist = artists.most_common(1)[0][0]

        print('\nSearching for {}:'.format(most_common_artist))

        tracks = vk_audio.search(q=most_common_artist, count=10)

        for self.n, self.track in enumerate(tracks, 1):
            print('{}. {} {}'.format(self.n, self.track['title'], self.track['url']))

    def getting_fields(self):
        session = vk.Session(access_token=self.access_token)
        vk_api_fields = vk.API(session)
        vk_api_fields.users.get(id=self.user_id,
                                fields='sex, city, interests, activities, music, movies, photo_400_orig')
        print(vk_api_fields)

    def in_dict(self):
        for _ in range(0, 15):
            self.dictionary = {'id': f'https://vk.com/{self.user_id}', '15 первых песен': [self.track['title']]}


VK_class = WorkWithVk(log_in, pass_word)
VK_class.LogIn()
VK_class.getting_15_audios()
# VK_class.getting_fields()