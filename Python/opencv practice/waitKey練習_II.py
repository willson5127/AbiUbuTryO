# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 17:21:19 2020

@author: willson

waitKey Test
"""

import cv2

lena = cv2.imread("lena.bmp")
cv2.imshow("demo", lena)
key = cv2.waitKey()
if key != -1:
    print("觸發了按鍵")
cv2.destroyAllWindows()