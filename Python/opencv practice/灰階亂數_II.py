# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 21:11:40 2020

@author: willson

gray random
"""
import numpy as np
import cv2

img = np.random.randint(0, 256, size = [256, 256], dtype = np.uint8)
cv2.imshow("demo", img)
cv2.waitKey()
cv2.destroyAllWindows()
