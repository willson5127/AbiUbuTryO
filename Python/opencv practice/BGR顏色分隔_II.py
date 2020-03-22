# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 15:56:26 2020

@author: willson

BGR split
"""
import cv2

lena = cv2.imread("lenacolor.png")
b, g, r = cv2.split(lena)
cv2.imshow("B", b)
cv2.imshow("G", g)
cv2.imshow("R", r)
cv2.waitKey()
cv2.destroyAllWindows()
