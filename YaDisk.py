import yadisk
from secret import yandex_token
class YaDisk:
    def __init__(self):
        self.disk = yadisk.YaDisk(token=yandex_token)

    def test(self):
        print(print(list(self.disk.get_files())))


y = YaDisk()
y.disk.upload(r"images/096.JPG", "/Test_Dir/096.JPG")
