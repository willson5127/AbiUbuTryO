# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 18:48:58 2020

@author: willson

Gray to BGR
"""
import cv2
import numpy as np

img = np.random.randint(0, 256, size = [2, 4], dtype = np.uint8)
rst = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
print("img = \n", img)
print("rst = \n", rst)
