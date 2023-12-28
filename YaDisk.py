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
y.disk.download("/Test_Dir", "C:\\Users\\Андрей\\PycharmProjects\\OpenCV\\images\\image1")
