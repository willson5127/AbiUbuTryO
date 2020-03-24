# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 22:08:51 2020

@author: willson

remap practice
"""
import cv2
import numpy as np

img = np.random.randint(0, 256, size = [4, 5], dtype = np.uint8)
rows, cols = img.shape
mapx = np.ones(img.shape, np.float32) * 3
mapy = np.ones(img.shape, np.float32) * 0
rst = cv2.remap(img, mapx, mapy,cv2.INTER_LINEAR)
print("img = \n", img)
print("mapx = \n", mapx)
print("mapy = \n", mapy)
print("rst = \n", rst)