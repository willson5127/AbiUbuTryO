# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 20:10:34 2020

@author: willson

addWeighted practice
"""
import cv2
import numpy as np
img1 = np.ones((3,4), dtype = np.uint8) * 100
img2 = np.ones((3,4), dtype = np.uint8) * 10
gamma = 3
img3 = cv2.addWeighted(img1, 0,6, img2, 5, gamma)
print(img3)
