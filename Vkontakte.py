import vk_api
import vk_api.vk_api
from Social import Social
from secret import *

"""
https://vkhost.github.io/
"""


class Vkontakte(Social):
    def __init__(self, token=access_token):
        self.vk = vk_api.VkApi(token=token)

    def send_post(self):
        self.vk.method("wall.post", {
            'v': '5.199',
            'owner_id': -222103827,
            'message': 'message',
            'friends_only': 0,
            'from_group': 1,
            'attachments': "https://sun9-24.userapi.com/impf/DlL6XoI28NM6mhof0qfzHk-ZuZOYJM0-h-FUTA/0WJWM4D3iZc.jpg?size=500x500&quality=96&sign=38987bce630c408a1238a737a7d1ae31&type=album"
        })

    def send_msg(self, user_id: int, text: str):
        self.vk.method("messages.send", {
            "user_id": user_id,
            "message": text,
            "random_id": 6
        })


vk = Vkontakte()
vk.send_post()



