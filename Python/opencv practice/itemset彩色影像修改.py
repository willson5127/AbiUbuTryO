# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 14:22:57 2020

@author: willson

adj BGR image
"""
import cv2
import numpy as np

img = cv2.imread("lenacolor.png")
cv2.imshow("before", img)
print("存取img.item(0, 0, 0) = ", img.item(0, 0, 0))
print("存取img.item(0, 0, 1) = ", img.item(0, 0, 1))
print("存取img.item(0, 0, 2) = ", img.item(0, 0, 2))
for i in range(0, 50):
    for j in range(0, 100):
        for k in range(0, 3):
            img.itemset((i, j, k), 255)
cv2.imshow("after", img)
print("修改後img.item(0, 0, 0) = ", img.item(0, 0, 0))
print("修改後img.item(0, 0, 1) = ", img.item(0, 0, 1))
print("修改後img.item(0, 0, 2) = ", img.item(0, 0, 2))
cv2.waitKey()
cv2.destroyAllWindows()