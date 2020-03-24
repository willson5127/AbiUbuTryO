# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 23:35:36 2020

@author: willson

remap image from x-aixs, y-aixs
"""
import cv2
import numpy as np

img = cv2.imread("lena.bmp")
rows, cols = img.shape[:2]
mapx = np.zeros(img.shape[:2], np.float32)
mapy = np.zeros(img.shape[:2], np.float32)
for i in range(rows):
    for j in range(cols):
        mapx.itemset((i, j), cols - 1 - j)
        mapy.itemset((i, j), rows - 1 - i)
rst = cv2.remap(img, mapx, mapy, cv2.INTER_LINEAR)
cv2.imshow("original", img)
cv2.imshow("result", rst)
cv2.waitKey()
cv2.destroyAllWindows()
