# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 17:35:36 2020

@author: willson

destroyAllWindows practice
"""
import cv2

lena = cv2.imread("lena.bmp")
cv2.imshow("demo1", lena)
cv2.imshow("demo2", lena)
cv2.waitKey()
cv2.destroyAllWindows()