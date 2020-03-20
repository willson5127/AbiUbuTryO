# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 17:46:56 2020

@author: willson

array to grayimage
"""
import cv2
import numpy as np

img = np.zeros((8,8), dtype = np.uint8)
print ("img = \n", img)
cv2.imshow("one", img)
print ("讀取像素點img[0,3] =", img[0,3])
img[0,3] = 255
print ("修改後img = \n", img)
print ("讀取修改後像素點imgp[0,3] =", img[0,3])
cv2.imshow("two", img)
cv2.waitKey()
cv2.destroyAllWindows()
