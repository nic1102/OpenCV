import random

from scipy.spatial import Delaunay
import numpy as np
from Logger import Logger
from ImageFile import ImageFile
from Primitive import Triangle
import math
import cv2


class Triangulation(ImageFile):

    def __init__(self, path: str):
        super().__init__(path)
        self.triangles = list()
        self.smart_triangles = list()

    def triangulate(self, vertices: list):
        tri = Delaunay(vertices)
        self.triangles = tri.simplices.tolist()

    @staticmethod
    def get_color(first_point: tuple, second_point: tuple, third_point: tuple) -> tuple:
        color = (
            (first_point[0] + second_point[0] + third_point[0]) // 3,
            (first_point[1] + second_point[1] + third_point[1]) // 3,
            (first_point[2] + second_point[2] + third_point[2]) // 3
        )
        return color

    @staticmethod
    def is_color_same(first, second, distance) -> bool:
        return math.sqrt((first[0] - second[0]) ** 2
                         + (first[1] - second[1]) ** 2
                         + (first[2] - second[2]) ** 2) <= distance

    @staticmethod
    def is_common(first, second) -> bool:
        for i in range(0, 3, 1):
            for j in range(0, 3, 1):
                if (first.sides[i] == second.sides[j] or
                        tuple(reversed(first.sides[i])) == tuple(reversed(second.sides[j])) or
                        tuple(reversed(first.sides[i])) == second.sides[j] or
                        first.sides[i] or tuple(reversed(second.sides[j]))):
                    first.neighbors.append(second.number)
                    second.neighbors.append(first.number)
                    return True
                else:
                    return False

    def find_background_colors(self, colors_count: int):
        background_colors = list()
        for i in range(0, len(self.smart_triangles), 1):
            ...

    @staticmethod
    def find_common_colors(colors_count: int):
        ...

    def do_triangulation(self, max_corners: int, quality: float, min_distance: int):
        self.img = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
        corners = cv2.goodFeaturesToTrack(self.img, max_corners, quality, min_distance)
        corners = np.intp(corners)
        new_corners = list()
        for i in corners:
            x, y = i.ravel()
            new_corners.append((x, y))
        # new_corners.append((0,0))
        # new_corners.append((self.width - 1, 0))
        # new_corners.append((self.width - 1, self.height - 1))
        # new_corners.append((0, self.height - 1))
        self.triangulate(new_corners)
        for i in range(0, len(self.triangles), 1):
            triangle = (
                new_corners[self.triangles[i][0]],
                new_corners[self.triangles[i][1]],
                new_corners[self.triangles[i][2]]
            )
            fill = self.get_color(
                self.image.getpixel(triangle[0]),
                self.image.getpixel(triangle[1]),
                self.image.getpixel(triangle[2])
            )
            self.smart_triangles.append(
                Triangle(triangle, fill, i)
            )

        i, j = 0, 1

        while i < len(self.smart_triangles) - 1:
            while j < len(self.smart_triangles):
                if (self.is_common(self.smart_triangles[i], self.smart_triangles[j]) and
                        self.is_color_same(
                            self.smart_triangles[i].fill,
                            self.smart_triangles[j].fill, 15) and
                        self.smart_triangles[j].is_count is False):

                    self.smart_triangles[i].is_count = True
                    self.smart_triangles[j].is_count = True

                    self.smart_triangles[j].fill = self.smart_triangles[i].fill
                else:
                    self.smart_triangles[i].is_count = False
                    self.smart_triangles[j].is_count = False
                j += 1
            i += 1
        for i in range(0, len(self.smart_triangles), 1):
            self.draw.polygon(self.smart_triangles[i].triangle, self.smart_triangles[i].fill)
        self.image.save(r'results/' + self.file_name + '.png')
        Logger.send_log(self.width, self.height, self.file_name)

    def task(self, step: int, n: int):
        temp_array = list()
        for i in range(0, n, 1):
            temp_array.append(
                (random.randint(0, self.width - 1),
                 random.randint(0, self.height - 1))
            )
        self.triangulate(temp_array)
        for i in range(0, len(self.triangles), 1):
            triangle = (
                        temp_array[self.triangles[i][0]],
                        temp_array[self.triangles[i][1]],
                        temp_array[self.triangles[i][2]]
                        )
            fill = self.get_color(
                self.image.getpixel(triangle[0]),
                self.image.getpixel(triangle[1]),
                self.image.getpixel(triangle[2])
            )
            self.smart_triangles.append(Triangle(triangle, fill, i))

        i, j = 0, 0

        while i < len(self.smart_triangles) - 1:
            while j < len(self.smart_triangles):
                if (self.is_common(self.smart_triangles[i], self.smart_triangles[j]) and
                        self.is_color_same(self.smart_triangles[i].fill, self.smart_triangles[j].fill, 40) and
                        self.smart_triangles[j].is_counted is False):

                    self.smart_triangles[i].is_counted = True
                    self.smart_triangles[j].is_counted = True

                    self.smart_triangles[j].fill = self.smart_triangles[i].fill
                else:
                    self.smart_triangles[i].is_counted = False
                    self.smart_triangles[j].is_counted = False
                j += 1
            i += 1
        for i in range(0, len(self.smart_triangles), 1):
            self.draw.polygon(self.smart_triangles[i].triangle, self.smart_triangles[i].fill)
        self.image.save(r'results/' + self.file_name + '.png')
