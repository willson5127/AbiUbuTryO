# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 19:56:05 2020

@author: willson

BGR image adj
"""
import cv2

img = cv2.imread("lenacolor.png")
cv2.imshow("before", img)
print ("存取img[0, 0] = ", img[0, 0])
print ("存取img[0, 0, 0] = ", img[0, 0, 0])
print ("存取img[0, 0, 1] = ", img[0, 0, 1])
print ("存取img[0, 0, 2] = ", img[0, 0, 2])
print ("存取img[50, 0] = ", img[50, 0])
print ("存取img[100, 0] = ", img[100, 0])
#區域1
for i in range(0, 50):
    for j in range(0, 100):
        for k in range(0, 3):
            img[i, j, k] = 255
#區域2
for i in range(50, 100):
    for j in range(0, 100):
        img[i, j] = [128, 128, 128]
#區域3
for i in range(100, 150):
    for j in range(0, 100):
        img[i, j] = 0
cv2.imshow("after", img)
print ("修改後img[0, 0] = ", img[0, 0])
print ("修改後img[0, 0, 0] = ", img[0, 0, 0])
print ("修改後img[0, 0, 1] = ", img[0, 0, 1])
print ("修改後img[0, 0, 2] = ", img[0, 0, 2])
print ("修改後img[50, 0] = ", img[50, 0])
print ("修改後img[100, 0] = ", img[100, 0])

cv2.waitKey()
cv2.destroyAllWindows()