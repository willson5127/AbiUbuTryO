# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 17:30:53 2020

@author: willson

encrypt to face
"""
import cv2
import numpy as np

#讀取原始載體影像
lena = cv2.imread("lena.bmp", 0)
#讀取原始載體影像的shape值
r, c = lena.shape
mask = np.zeros((r, c), dtype = np.uint8)
mask[220:400, 250:350] = 1
#取得一個key,打碼、解碼所使用的金鑰
key = np.random.randint(0, 256, size = [r, c], dtype = np.uint8)
#===============取得打碼臉==================
#使用金鑰key對原始影像lena加密
lenaXorKey = cv2.bitwise_xor(lena, key)
#取得加密影像的臉部資訊encryptFace
encryptFace = cv2.bitwise_and(lenaXorKey, mask * 255)
#將影像lena內的臉部值設定為0,獲得noFace1
noFace1 = cv2.bitwise_and(lena, (1 - mask) * 255)
#獲得打碼的lena影像
maskFace = encryptFace + noFace1
#==============將打碼臉打碼==================
#將臉部打碼的lena與金鑰key進行互斥運算,獲得臉部的原始資訊
extractOriginal = cv2.bitwise_xor(maskFace, key)
#將解碼的臉部資訊rxtractOriginal分析出來,獲得extractFace
extractFace = cv2.bitwise_and(extractOriginal, mask * 255)
#從臉部打碼的lena內分析沒有臉部資訊的lena影像,獲得noFace2
noFace2 = cv2.bitwise_and(maskFace, (1 - mask) * 255)
#獲得解碼的lena影像
extractLena = noFace2 + extractFace
#==============顯示影像=======================
cv2.imshow("lena", lena)
cv2.imshow("mask", mask * 255)
cv2.imshow("1 - mask", (1 - mask) * 255)
cv2.imshow("key", key)
cv2.imshow("lenaXorKey", lenaXorKey)
cv2.imshow("encryptFace", encryptFace)
cv2.imshow("noFace1", noFace1)
cv2.imshow("maskFace", maskFace)
cv2.imshow("extractOriginal", extractOriginal)
cv2.imshow("extractFace", extractFace)
cv2.imshow("noFace2", noFace2)
cv2.imshow("extractLena", extractLena)
cv2.waitKey()
cv2.destroyAllWindows()