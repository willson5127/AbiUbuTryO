# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 17:16:19 2020

@author: willson

cv2.waitKey() practice
"""
import cv2

lena = cv2.imread("lena.bmp")
cv2.imshow("demo", lena)
key = cv2.waitKey()
if key == ord('A'):
    cv2.imshow("PressA", lena)
if key == ord('B'):
    cv2.imshow("PressB", lena)
cv2.waitKey()
cv2.destroyAllWindows()