# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 17:11:19 2020

@author: willson

show image at window
"""
import cv2

lena = cv2.imread("lena.bmp")
cv2.namedWindow("lesson")
cv2.imshow("lesson", lena)
cv2.waitKey()
cv2.destroyAllWindows()
