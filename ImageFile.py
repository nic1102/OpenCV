from PIL import Image
from PIL import ImageDraw
import uuid
import cv2


class ImageFile:
    def __init__(self, path: str):
        self.path = path
        self.image = Image.open(self.path)
        self.draw = ImageDraw.Draw(self.image)
        self.width = self.image.size[0]
        self.height = self.image.size[1]
        self.pix = self.image.load()
        self.img = cv2.imread(path)
        self.file_name = str(uuid.uuid4())

    @staticmethod
    def __new_image(color: tuple, size: tuple):
        return Image.new('RGB', size, color)
