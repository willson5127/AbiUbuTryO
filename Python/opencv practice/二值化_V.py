# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 05:53:15 2020

@author: willson

thresthold truncate array
"""
import cv2
import numpy as np

img = np.random.randint(0, 256, size = [4, 5], dtype = np.uint8)
t, rst = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)
print("img = \n", img)
print("t = \n", t)
print("rst = \n", rst)
