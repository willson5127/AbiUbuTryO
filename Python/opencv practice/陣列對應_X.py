# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 23:42:15 2020

@author: willson

remap to rotate
"""
import cv2
import numpy as np

img = np.random.randint(0, 256, size = [4, 6], dtype = np.uint8)
rows, cols = img.shape
mapx = np.zeros(img.shape, np.float32)
mapy = np.zeros(img.shape, np.float32)
for i in range(rows):
    for j in range(cols):
        mapx.itemset((i, j), i)
        mapy.itemset((i, j), j)
rst = cv2.remap(img, mapx, mapy, cv2.INTER_LINEAR)
print("img = \n", img)
print("mapx = \n", mapx)
print("mapy = \n", mapy)
print("rst = \n", rst)
