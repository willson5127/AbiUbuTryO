# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 20:47:14 2020

@author: willson

random array
"""
import numpy as np

img = np.random.randint(10, 99, size = [5, 5], dtype = np.uint8)
print ("img = \n", img)
print ("讀取像素點img.item(3,2) = ", img.item(3, 2))
img.itemset((3, 2), 255)
print ("修改後img = \n", img)
print ("修改後像素點img.item(3, 2) = ", img.item(3, 2))
