# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 19:58:40 2020

@author: willson

add process
"""
import numpy as np

img1 = np.random.randint(0, 256, size = [3, 3], dtype = np.uint8)
img2 = np.random.randint(0, 256, size = [3, 3], dtype = np.uint8)
print("img1 = \n", img1)
print("img2 = \n", img2)
print("img1 + img2 = \n", img1 + img2)
