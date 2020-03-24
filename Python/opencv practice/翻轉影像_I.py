# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 21:25:17 2020

@author: willson

flip image
"""
import cv2

img = cv2.imread("lena.bmp")
x = cv2.flip(img, 0)
y = cv2.flip(img, 1)
xy = cv2.flip(img, -1)
cv2.imshow("img", img)
cv2.imshow("x", x)
cv2.imshow("y", y)
cv2.imshow("xy", xy)
cv2.waitKey()
cv2.destroyAllWindows()
