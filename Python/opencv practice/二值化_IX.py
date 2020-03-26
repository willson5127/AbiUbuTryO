# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 06:46:42 2020

@author: willson

threshold tozero array
"""
import cv2
import numpy as np

img = np.random.randint(0, 256, size = [4, 5], dtype = np.uint8)
t, rst = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
print("img = \n", img)
print("t = ", t)
print("rst = \n", rst)
