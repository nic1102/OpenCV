from scipy.spatial import Delaunay
import numpy as np
from PIL import Image
from PIL import ImageDraw

from ImageFile import ImageFile
from Primitive import Triangle
import math
import cv2
import uuid


class Triangulation(ImageFile):

    def __init__(self, path):
        super().__init__(path)
        self.triangles = []
        self.smart_triangles = []

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

    def do_triangulation(self, max_corners, quality, min_distance):
        self.img = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
        corners = cv2.goodFeaturesToTrack(self.img, max_corners, quality, min_distance)
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
            fill = self.get_color(self.img, self.image.getpixel(triangle[0]), self.image.getpixel(triangle[1]), self.image.getpixel(triangle[2]))
            number = i
            self.smart_triangles.append(Triangle(triangle, fill, number))
        print(len(self.smart_triangles))
        i = 0
        j = 1

        while i < len(self.smart_triangles) - 1:
            while j < len(self.smart_triangles):
                if self.is_common(self.smart_triangles[i], self.smart_triangles[j]) and self.is_color_same(self.smart_triangles[i].fill,
                                                                                       self.smart_triangles[j].fill, 15) and \
                        self.smart_triangles[j].is_count == False:
                    # smart_triangles[i].neighbors.append(smart_triangles[j].number)
                    # smart_triangles[j].neighbors.append(smart_triangles[i].number)

                    self.smart_triangles[i].is_count = True
                    self.smart_triangles[j].is_count = True

                    self.smart_triangles[j].fill = self.smart_triangles[i].fill
                    # draw.polygon(smart_triangles[j].triangle, fill=smart_triangles[j].fill)

                else:
                    self.smart_triangles[i].is_count = False
                    self.smart_triangles[j].is_count = False

                    # smart_triangles.pop(j)
                j += 1
            i += 1
        for i in range(0, len(self.smart_triangles), 1):
            self.draw.polygon(self.smart_triangles[i].triangle, self.smart_triangles[i].fill)
        self.image.save(r'Z:\Results\\' + str(uuid.uuid4()) + 'result.png')