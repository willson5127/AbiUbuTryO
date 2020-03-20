# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 17:56:06 2020

@author: willson

BGR array generat
"""
import numpy as np
import cv2
#=================blue==============
blue = np.zeros((300, 300, 3), dtype = np.uint8)
blue[:, :, 0] = 255
print ("blue = \n", blue)
cv2.imshow("blue", blue)
#================Green================
green = np.zeros((300, 300, 3), dtype = np.uint8)
green[:, :, 1] = 255
print ("green = \n", green)
cv2.imshow("green", green)
#================Red==================
red = np.zeros((300, 300, 3), dtype = np.uint8)
red[:, :, 2] = 255
print ("red = \n", red)
cv2.imshow("red", red)
#===============relase screen=========
cv2.waitKey()
cv2.destroyAllWindows()
