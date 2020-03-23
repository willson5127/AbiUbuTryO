# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 21:00:20 2020

@author: willson

BGR to RGB
"""
import cv2

lena = cv2.imread("lenacolor.png")
rgb = cv2.cvtColor(lena, cv2.COLOR_BGR2RGB)
cv2.imshow("lena", lena)
cv2.imshow("rgb", rgb)
cv2.waitKey()
cv2.destroyAllWindows()
