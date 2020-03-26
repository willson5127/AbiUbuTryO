# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 08:44:03 2020

@author: willson

blur image
"""
import cv2

o = cv2.imread("lena.bmp")
r5 = cv2.blur(o, (5, 5))
r30 = cv2.blur(o, (30, 30))
cv2.imshow("original", o)
cv2.imshow("result5", r5)
cv2.imshow("result30", r30)
cv2.waitKey()
cv2.destroyAllWindows()
