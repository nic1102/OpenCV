from scipy.spatial import Delaunay
import numpy as np
from PIL import Image
from PIL import ImageDraw
from Primitive import Triangle
import random
import math
import cv2
import uuid

class Triangulation:

    def __init__(self, path):
        self.triangles = []
        self.smart_triangles = []
        self.path = path

    def triangulate(self, vertices):
        tri = Delaunay(vertices)
        self.triangles = tri.simplices.tolist()
        
    @staticmethod
    def get_color(self, img, first_point, second_point, third_point):
        color = (
                (first_point[0] + second_point[0] + third_point[0]) // 3,
                (first_point[1] + second_point[1] + third_point[1]) // 3,
                (first_point[2] + second_point[2] + third_point[2]) // 3
        )
        return color

    @staticmethod
    def is_color_same(self, first, second, distance):
        if math.sqrt(
                (first[0] - second[0]) ** 2 + (first[1] - second[1]) ** 2 + (first[2] - second[2]) ** 2) <= distance:
            return True
        else:
            return False

    @staticmethod
    def is_common(self, first, second):
        for i in range(0, 3, 1):
            for j in range(0, 3, 1):
                if (first.sides[i] == second.sides[j] or list(reversed(first.sides[i])) == list(
                        reversed(second.sides[j]))):
                    first.neighbors.append(second.numero)
                    second.neighbors.append(first.numero)
                    return True
                else:
                    return False

    def __pillow_init(self):
        # image = Image.new('RGB', (width, height), "#000000")
        image = Image.open(self.path)
        # image = Image.new("RGB", size = (6000,4000))
        draw = ImageDraw.Draw(image)
        self.width = image.size[0]
        self.height = image.size[1]
        pix = image.load()

    def do_triangulation(self):
        img = cv2.imread(self.path)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        corners = cv2.goodFeaturesToTrack(img, 500000, 0.0001, 25)
        corners = np.intp(corners)
        new_corners = []
        for i in corners:
            x, y = i.ravel()
            new_corners.append((x, y))
        self.triangulate(new_corners)



        for i in range(0, len(self.triangles), 1):
            first = self.triangles[i][0]
            second = self.triangles[i][1]
            third = self.triangles[i][2]
            triangle = (new_corners[first], new_corners[second], new_corners[third])
            fill = self.get_color(img, image.getpixel(triangle[0]), image.getpixel(triangle[1]), image.getpixel(triangle[2]))
            numero = i
            smart_triangles.append(Triangle(triangle, fill, numero))
        print(len(smart_triangles))
        i = 0
        j = 1

        while i < len(smart_triangles) - 1:
            while j < len(smart_triangles):
                if self.is_common(smart_triangles[i], smart_triangles[j]) and self.is_color_same(smart_triangles[i].fill,
                                                                                       smart_triangles[j].fill, 15) and \
                        smart_triangles[j].is_count == False:
                    # smart_triangles[i].neighbors.append(smart_triangles[j].numero)
                    # smart_triangles[j].neighbors.append(smart_triangles[i].numero)

                    smart_triangles[i].is_count = True
                    smart_triangles[j].is_count = True

                    smart_triangles[j].fill = smart_triangles[i].fill
                    # draw.polygon(smart_triangles[j].triangle, fill=smart_triangles[j].fill)

                else:
                    smart_triangles[i].is_count = False
                    smart_triangles[j].is_count = False

                    # smart_triangles.pop(j)
                j += 1
            i += 1



        for i in range(0, len(smart_triangles), 1):
            draw.polygon(smart_triangles[i].triangle, fill=smart_triangles[i].fill)


        image.save(r'Z:\Results\\' + str(uuid.uuid4()) + 'result.png')