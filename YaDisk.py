import yadisk
from secret import yandex_token


class YaDisk:
    def __init__(self):
        self.disk = yadisk.YaDisk(token=yandex_token)

    def save_images(self, images: list, is_raw: bool):
        ...

    def check_raw_images(self):
        ...





y = YaDisk()
y.disk.upload(r"images/096.JPG", "/Test_Dir/096.JPG")
