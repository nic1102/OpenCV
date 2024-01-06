import yadisk
from secret import yandex_token


class YaDisk:
    def __init__(self):
        self.disk = yadisk.YaDisk(token=yandex_token)

    def save_images(self, images: list, is_raw: bool):
        if self.disk.check_token():
            ...
        else:
            return NotImplemented

    def get_dir_info(self, dir_name='/Test_Dir/1'):
        for item in self.disk.listdir(dir_name):
            print(f"Название: {item['name']}")
            print(f'Размер: {item["size"]} байт')
            print(f"Тип файла: {item['type']}")
            print(f"Тип документа: {item['media_type']}")
            print(f"Дата создания: {item['created']}\n")

    def check_raw_images(self):
        NotImplemented


y = YaDisk()
y.get_dir_info()
