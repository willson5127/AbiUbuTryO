# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 21:16:34 2020

@author: willson

adj gray image
"""
import cv2

img = cv2.imread("lena.bmp", 0)
#測試讀取、修改單一像素質
print ("讀取像素點img.item(3, 2) = ", img.item(3, 2))
img.itemset((3, 2), 255)
print ("修改後像素點img.item(3, 2) = ", img.item(3,2))
#測試修改一個區域的像素值
cv2.imshow("before", img)
for i in range(10, 100):
    for j in range(80, 100):
        img.itemset((i, j), 255)
cv2.imshow("after", img)
cv2.waitKey()
cv2.destroyAllWindows()
