# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 18:42:40 2020

@author: willson

BGR to gray
"""
import cv2
import numpy as np

img = np.random.randint(0, 256, size = [2, 4, 3], dtype = np.uint8)
rst = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
print("img = \n", img)
print("rst = \n", rst)
print("像素點(1, 0) 直接計算獲得的值 = ", img[1, 0, 0] * 0.114 + img[1, 0, 1] * 0.587 + img[1, 0, 2] * 0.299)
print("像素點(1, 0) 使用公式cv2.cvtColor() 轉換值 = ", rst[1, 0])
