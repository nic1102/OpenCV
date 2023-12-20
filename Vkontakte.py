import time
import vk_api
import vk_api.vk_api
from vk_api.bot_longpoll import VkBotLongPoll
from vk_api.bot_longpoll import VkBotEventType


access_token = "vk1.a.IbgNFEG8e6gaHaQINxH1CxAWud52BjgoBwrJPcYMBvZbIQMxryKWGdrdOzwWobvVTW00wCP1aF4hrGmvEWaiD4t9Y1TDu9yvCloWSAZsdnCjh8-8ft8_qMKrfRHglQiSkP7zLewyoLh6mmI3YyCdEuavLRtJYCKcyHnxNREF-R1Te2jCfCq3ztifHqBXv6u8DFEcB-LS0Iol8Z9sHfCH5Q"
group_token = "vk1.a.UqK1lMyd_GMIhA-Lry6ve_W3duA-av1Q6Bl6QMRTqz6vE6JpOk4dC5j-j8zZyXm3wXTnWPlEnr2ELAoGLwoPzCe2YtDeKkZZrK4E31P93q5zRNFufvVuldT3vSUqyGPhz8fbCbXKAmSIUKxtpOcPkhG42T5mqlS35hndVOb52Kxdk0KNXbNpsn2ULCMWsvUhySufPleBvCiP45VVxiapVw"
private_key = "mTaVfYcwuf1p3Fuyvvem"
service_key = "78b5aba078b5aba078b5aba0a97ba00ae8778b578b5aba01db747a44ff30bbf56d8b2d7"
secret_key = "ccf94906195f991a20"
vk = vk_api.VkApi(token = group_token)


def create_post():
    vk.method("wall.post",{
        'v': '5.107',
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
        "random_id": 4
    })


send_msg(162863885,"gasfawdas")
