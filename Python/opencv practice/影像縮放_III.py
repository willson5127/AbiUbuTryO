# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 21:21:42 2020

@author: willson

resize image
"""
import cv2

img = cv2.imread("lena.bmp")
rst = cv2.resize(img, None, fx = 2, fy = 0.5)
print("img.shape = ", img.shape)
print("rst.shape = ", rst.shape)
