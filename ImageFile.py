import os.path
import PIL
from PIL import Image
from PIL import ImageDraw
from config import image_size
import cv2

class ImageFile:
    def __init__(self, path):
        self.path = path
        self.image = Image.open(self.path)
        self.draw = ImageDraw.Draw(self.image)
        self.width = self.image.size[0]
        self.height = self.image.size[1]
        self.pix = self.image.load()
        self.img = cv2.imread(path)

    @staticmethod
    def __new_image(self, color, size: tuple):
        image = Image.new('RGB', size, color)
