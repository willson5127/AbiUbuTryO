# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 21:11:23 2020

@author: willson

resize image
"""
import cv2

img = cv2.imread("lena.bmp")
rows, cols = img.shape[:2]
size = (int(cols * 0.9), int(rows * 0.5))
rst = cv2.resize(img, size)
print("img.shape = ", img.shape)
print("rst.shape = ", rst.shape)

