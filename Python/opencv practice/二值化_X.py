# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 07:04:21 2020

@author: willson

threshold tozero image
"""
import cv2

img = cv2.imread("lena.bmp")
t, rst = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
cv2.imshow("img", img)
cv2.imshow("rst", rst)
cv2.waitKey()
cv2.destroyAllWindows()
