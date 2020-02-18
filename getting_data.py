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
    def __init__(self, login, password):
        self.login = login
        self.password = password
        self.VK = None

    def LogIn(self):
        self.VK = vk_api.VkApi(self.login, self.password, auth_handler=auth_handler)
        self.VK.auth()
        VK_auth = self.VK.get_api()
        access_token = 0

        try:
            User = VK_auth.users.get()
        except Exception as e:
            print(e)
        else:
            print(f"\nHello {User[0]['first_name']}")

            with open('vk_config.v2.json', 'r') as data_file:
                data = json.load(data_file)
                print(data)

            for xxx in data[self.login]['token'].keys():
                for yyy in data[self.login]['token'][xxx].keys():
                    access_token = data[self.login]['token'][xxx][yyy]['access_token']

            print('=' * 85)
            print(f"Твой ID {User[0]['id']}")
            user_id = User[0]['id']
            print('=' * 85)
            print(f"Access_Token: {access_token}")
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

        for n, track in enumerate(tracks, 1):
            print('{}. {} {}'.format(n, track['title'], track['url']))

    def getting_fields(self):
        vk_profile = self.VK.auth()
        vk_profile.fields()


VK_class = WorkWithVk(log_in, pass_word)
VK_class.LogIn()
VK_class.getting_15_audios()
