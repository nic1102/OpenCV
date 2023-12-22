import time
import vk_api
import vk_api.vk_api
from vk_api.bot_longpoll import VkBotLongPoll
from vk_api.bot_longpoll import VkBotEventType
from secret import *
import requests

vk = vk_api.VkApi(token = access_token)

def create_post():
    vk.method("wall.post", {
        'v': '5.199',
        'access_token': access_token,
        'owner_id': -1,
        'message': 'message',
        'friends_only': 0,
        'from_group': 1
    })

def send_msg(user_id,text):
    vk.method("messages.send", {
        "user_id": user_id,
        "message": text,
        "random_id": 6
    })

create_post()