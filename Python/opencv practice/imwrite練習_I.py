# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 17:39:34 2020

@author: willson

imwrite practice
"""
import cv2

lena = cv2.imread("lena.bmp")
r = cv2.imwrite("result.bmp", lena)
