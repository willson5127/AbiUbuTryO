# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 14:24:09 2020

@author: willson

array add process
"""
import cv2
import numpy as np

img1 = np.ones((4, 4), dtype = np.uint8) * 3
img2 = np.ones((4, 4), dtype = np.uint8) * 5
print("img1 = \n", img1)
print("img2 = \n", img2)
img3 = cv2.add(img1, img2)
print("cv2.add(img1, img2) = \n", img3)
img4 = cv2.add(img1, 6)
print("cv2.add(img1, 6) = \n", img4)
img5 = cv2.add(6, img2)
print("cv2.add(6, img2) = \n", img5)
