# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 08:39:32 2020

@author: willson

blur practice
"""
import cv2

o = cv2.imread("lena.bmp")
r = cv2.blur(o, (5, 5))
cv2.imshow("original", o)
cv2.imshow("result", r)
cv2.waitKey()
cv2.destroyAllWindows()
