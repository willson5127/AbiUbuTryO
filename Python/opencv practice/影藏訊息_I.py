# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 13:59:25 2020

@author: willson

hid the information
"""
import cv2
import numpy as np

img1 = np.ones((4, 4), dtype = np.uint8) * 3
img2 = np.ones((4, 4), dtype = np.uint8) * 5
mask = np.zeros((4, 4), dtype = np.uint8)
mask[2:4, 2:4] = 1
img3 = np.ones((4, 4), dtype = np.uint8) * 66
print("img1 = \n", img1)
print("img2 = \n", img2)
print("mask = \n", mask)
print("初值img3 = \n", img3)
img3 = cv2.add(img1, img2, mask = mask)
print("求和後img3 = \n", img3)
