# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 14:17:27 2020

@author: willson

RGB random image
"""
import cv2
import numpy as np

img = np.random.randint(0, 256, size = [256, 256, 3], dtype = np.uint8)
cv2.imshow("demo", img)
cv2.waitKey()
cv2.destroyAllWindows()
