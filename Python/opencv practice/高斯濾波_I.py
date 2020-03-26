# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 19:17:32 2020

@author: willson

GaussianBlur practice
"""
import cv2

o = cv2.imread("lenacolor.png", 0)
r = cv2.GaussianBlur(o, (5, 5), 0, 0)
cv2.imshow("original", o)
cv2.imshow("result", r)
cv2.waitKey()
cv2.destroyAllWindows()
