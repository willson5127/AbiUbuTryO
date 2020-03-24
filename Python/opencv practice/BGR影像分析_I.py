# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 18:33:24 2020

@author: willson

scan Opencv icon color
"""
import cv2
import numpy as np

opencv = cv2.imread("opencv.jpg")
hsv = cv2.cvtColor(opencv, cv2.COLOR_BGR2HSV)
cv2.imshow('opencv', opencv)
#===================指定藍色值的範圍===========================
minBlue = np.array([110, 50, 50])
maxBlue = np.array([130, 255, 255])
#確定藍色區域
mask = cv2.inRange(hsv, minBlue, maxBlue)
#透過隱藏控制的逐位元與運算,鎖定藍色區域
blue = cv2.bitwise_and(opencv, opencv, mask = mask)
cv2.imshow('blue', blue)
#==================指定綠色值的範圍============================
minGreen = np.array([50, 50, 50])
maxGreen = np.array([70, 255, 255])
#確定綠色區域
mask = cv2.inRange(hsv, minGreen, maxGreen)
#透過影藏控制的逐位元與運算,鎖定藍色區域
green = cv2.bitwise_and(opencv, opencv, mask = mask)
cv2.imshow('green', green)
#==================指定紅色值的範圍============================
minRed = np.array([0, 50, 50])
maxRed = np.array([30, 255, 255])
#確定紅色區域
mask = cv2.inRange(hsv, minRed, maxRed)
#透過隱藏控制的逐位元與運算,鎖定紅色區域
red = cv2.bitwise_and(opencv, opencv, mask = mask)
cv2.imshow('red', red)
cv2.waitKey()
cv2.destroyAllWindows()
