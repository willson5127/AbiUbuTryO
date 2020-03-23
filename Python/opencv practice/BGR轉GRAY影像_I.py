# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 20:47:30 2020

@author: willson

BGR to Gray image
"""
import cv2

lena = cv2.imread("lenacolor.png")
gray = cv2.cvtColor(lena, cv2.COLOR_BGR2GRAY)
rgb = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
#==================列印shape==================
print("lena.shape = ", lena.shape)
print("gray.shape = ", gray.shape)
print("rgb.shape = ", rgb.shape)
#==================顯示結果===================
cv2.imshow("lena", lena)
cv2.imshow("gray", gray)
cv2.imshow("rgb", rgb)
cv2.waitKey()
cv2.destroyAllWindows()
