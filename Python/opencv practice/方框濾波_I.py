# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 16:30:41 2020

@author: willson

boxFilter practice
"""
import cv2

o = cv2.imread("lenacolor.png", 0)
r = cv2.boxFilter(o, -1, (5, 5))
cv2.imshow("original", o)
cv2.imshow("result", r)
cv2.waitKey()
cv2.destroyAllWindows()
