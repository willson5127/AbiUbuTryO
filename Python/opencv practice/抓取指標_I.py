# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 18:06:04 2020

@author: willson

inRange practice
"""
import cv2
import numpy as np

img = np.random.randint(0, 256, size = [5, 5], dtype = np.uint8)
min = 100
max = 200
mask = cv2.inRange(img, min, max)
print("img = \n", img)
print("mask = \n", mask)
