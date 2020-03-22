# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 16:16:52 2020

@author: willson

contant with image
"""
import cv2

gray = cv2.imread("lena.bmp", 0)
color = cv2.imread("lenacolor.png")
print("影像gray屬性:")
print("gray.shape = ", gray.shape)
print("gray.size = ", gray.size)
print("gray.dtype = ", gray.dtype)
print("影像color屬性:")
print("color.shape = ", color.shape)
print("color.size = ", color.size)
print("color.dtype = ", color.dtype)
