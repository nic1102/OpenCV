import cv2
import PIL
import time
from PIL import Image
from PIL import ImageDraw
import numpy as np
from numpy import *
import uuid
from scipy.spatial import Delaunay
from Primitive import Triangle

def triangulate(vertices):
    tri = Delaunay(vertices)
    triangles = tri.simplices.tolist()
    return triangles

def get_corners(n):
    corners = []
    for i in range(0,n,1):
        corners.append((random.randint(0,6000),random.randint(0,4000)))
    return corners

def get_color(img, first_point, second_point, third_point):
    red = (first_point[0] + second_point[0] + third_point[0]) // 3
    green = (first_point[1] + second_point[1] + third_point[1]) // 3
    blue = (first_point[2] + second_point[2] + third_point[2]) // 3
    color = (red, green, blue)
    return color

def is_color_same(first, second, distance):
    if (math.sqrt((first[0] - second[0]) ** 2 + (first[1] - second[1]) ** 2 + (first[2] - second[2]) ** 2) <= distance):
        return True
    else:
        return False

def is_common(first, second):
    for i in range(0,3,1):
        for j in range(0,3,1):
            if (first.sides[i] == second.sides[j] or list(reversed(first.sides[i])) == list(reversed(second.sides[j]))):
                first.neighbors.append(second.numero)
                second.neighbors.append(first.numero)
                return True
            else:
                return False

if __name__ == "__main__":
    start = time.perf_counter()
    img = cv2.imread('images/test_4.jpg')
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    new_img = np.zeros(img.shape, dtype="uint8")

    corners = cv2.goodFeaturesToTrack(img, 500000, 0.0001, 10)
    corners = np.intp(corners)
    new_corners = []
    for i in corners:
        x, y = i.ravel()
        new_corners.append((x, y))
        cv2.circle(new_img,(x,y),5,(255,0,0), -1)
    print(new_corners)
    print(len(new_corners))
    triangles = triangulate(new_corners)
    print(triangles)



    # image = Image.new('RGB', (width, height), "#000000")
    image = Image.open("images/test_4.jpg")
    #image = Image.new("RGB", size = (6000,4000))
    draw = ImageDraw.Draw(image)
    width = image.size[0]
    height = image.size[1]
    pix = image.load()

    smart_triangles = []

    for i in range(0, len(triangles), 1):
        first = triangles[i][0]
        second = triangles[i][1]
        third = triangles[i][2]
        triangle = (new_corners[first], new_corners[second], new_corners[third])
        fill = get_color(img, image.getpixel(triangle[0]), image.getpixel(triangle[1]), image.getpixel(triangle[2]))
        numero = i
        smart_triangles.append(Triangle(triangle, fill, numero))
    print(len(smart_triangles))
    i = 0
    j = 1


    while(i<len(smart_triangles)-1):
        while(j<len(smart_triangles)):
            if (is_common(smart_triangles[i],smart_triangles[j]) and is_color_same(smart_triangles[i].fill,smart_triangles[j].fill,15) and smart_triangles[j].is_count == False):
                #smart_triangles[i].neighbors.append(smart_triangles[j].numero)
                #smart_triangles[j].neighbors.append(smart_triangles[i].numero)

                smart_triangles[i].is_count = True
                smart_triangles[j].is_count = True

                smart_triangles[j].fill = smart_triangles[i].fill
                #draw.polygon(smart_triangles[j].triangle, fill=smart_triangles[j].fill)

            else:
                smart_triangles[i].is_count = False
                smart_triangles[j].is_count = False

                #smart_triangles.pop(j)
            j += 1
        i += 1
    print(f"j- {j}")

    print(len(smart_triangles))
    print(smart_triangles[2].triangle)

    for i in range(0,len(smart_triangles),1):
        draw.polygon(smart_triangles[i].triangle, fill=smart_triangles[i].fill)

    #print(fill)
    #print(triangle)
    image.save(r'Z:\Results\\' + str(uuid.uuid4()) + 'result.png')
    #image.show()
    #image.show()

    #cv2.waitKey(0)
    #cv2.imwrite("Z:\\Results\\" + uuid.uuid4().__str__() + ".jpg", new_img)
    finish = time.perf_counter()
    print(f"Время выполнения - {finish-start}")