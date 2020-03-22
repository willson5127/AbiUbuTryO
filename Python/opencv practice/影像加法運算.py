# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 20:06:36 2020

@author: willson

add process image
"""
import cv2

a = cv2.imread("lena.bmp", 0)
b = a
result1 = a + b
result2 = cv2.add(a, b)
cv2.imshow("original", a)
cv2.imshow("result1", result1)
cv2.imshow("result2", result2)
cv2.waitKey()
cv2.destroyAllWindows()