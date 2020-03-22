# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 14:32:11 2020

@author: willson

get ROI from face
"""
import cv2

a = cv2.imread("lenacolor.png", cv2.IMREAD_UNCHANGED)
face = a[220:400, 250:350]
cv2.imshow("original", a)
cv2.imshow("face", face)
cv2.waitKey()
cv2.destroyAllWindows()
