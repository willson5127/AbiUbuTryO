# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 17:31:43 2020

@author: willson

cv2.destroyWindow practice
"""
import cv2

lena = cv2.imread("lena.bmp")
cv2.imshow("demo", lena)
cv2.waitKey()
cv2.destroyWindow("demo")
