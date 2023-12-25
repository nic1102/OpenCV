import vk_api
import vk_api.vk_api
from Social import Social
from secret import *


class Vkontakte(Social):
    def __init__(self, token=access_token):
        self.vk = vk_api.VkApi(token=token)

    def send_post(self):
        self.vk.method("wall.post", {
            'v': '5.199',
            'access_token': access_token,
            'owner_id': -1,
            'message': 'message',
            'friends_only': 0,
            'from_group': 1
        })

    def send_msg(self, user_id, text):
        self.vk.method("messages.send", {
            "user_id": user_id,
            "message": text,
            "random_id": 6
        })


vk = Vkontakte()
vk.send_post()



