import json

import yadisk
from secret import yandex_token


class YaDisk:

    """
    Image_Bot/Raw
    Image_Bot/New
    """

    def __init__(self):
        self.disk = yadisk.YaDisk(token=yandex_token)
        self.last_time = None
        self.last_dir = None

    def save_images(self, images: list, is_raw: bool):
        if self.disk.check_token():
            ...
        else:
            return NotImplemented

    def get_dir_info(self, dir_name='/Test_Dir/1'):
        for item in self.disk.listdir(dir_name):
            print(f"Name: {item['name']}")
            print(f'Size: {item["size"]} byte')
            print(f"File type: {item['type']}")
            print(f"Document type: {item['media_type']}")
            print(f"Creation date: {item['created']}\n")


    def check_raw_images(self):
        with open("src/last_dir.json") as result:
            r = json.load(result)
        self.last_time = r["last_post_time"]
        self.last_dir = r["last_post_dir"]


y = YaDisk()
y.get_dir_info()