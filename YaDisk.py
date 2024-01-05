import yadisk
from secret import yandex_token


class YaDisk:
    def __init__(self):
        self.disk = yadisk.YaDisk(token=yandex_token)

    def save_images(self, images: list, is_raw: bool):
        if self.disk.check_token(): #Проверка токена
            ...
        else:
            return NotImplemented
    def check_raw_images(self):
        ...

y = YaDisk()
print(list(y.disk.listdir("/Test_Dir")))
