# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 21:41:59 2020

@author: willson

BGR array random
"""
import numpy as np

img = np.random.randint(10, 99, size = [2, 4, 3], dtype = np.uint8)
print ("img = \n", img)
print ("讀取像素點img[1, 2, 0] = ", img.item(1, 2, 0))
print ("讀取像素點img[0, 2, 1] = ", img.item(0, 2, 1))
print ("讀取像素點img[1, 0, 2] = ", img.item(1, 0, 2))
img.itemset((1, 2, 0), 255)
img.itemset((0, 2, 1), 255)
img.itemset((1, 0, 2), 255)
print("修改後img = \n", img)
print("修改後像素點img[1, 2, 0] = ", img.item(1, 2, 0))
print("修改後像素點img[0, 2, 1] = ", img.item(0, 2, 1))
print("修改後像素點img[1, 0, 2] = ", img.item(1, 0, 2))