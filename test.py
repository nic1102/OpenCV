import cv2
import uuid
import numpy as np

img = cv2.imread('images/test_4.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
thresh_img = cv2.adaptiveThreshold(img,128,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,1999,0)
contours, hierarchy = cv2.findContours(thresh_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(img, contours, -1, (255, 255, 255), 1)

cv2.imwrite("Z:\\Results\\" + uuid.uuid4().__str__() + ".jpg", img)
