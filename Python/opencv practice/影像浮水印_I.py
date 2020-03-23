# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 16:42:44 2020

@author: willson

wartermark in image
"""
import cv2
import numpy as np
#讀取原始載體影像
lena = cv2.imread("lena.bmp", 0)
#讀取原始載體影像的shape值
r, c = lena.shape
#讀取浮水印影像
watermark = cv2.imread("watermark.bmp", 0)
watermark = cv2.resize(watermark, (r, c), interpolation=cv2.INTER_CUBIC)
cv2.imshow("org", watermark)
#將浮水印影像內的值255處理為1,以方便嵌入
#後續章節會介紹使用threshold處理
w = watermark[:, :] > 150
a = watermark[:, :] <= 150
watermark[w] = 1
watermark[a] = 0
#===============嵌入過程=================
#產生元素值都是254的陣列
t254 = np.ones((r, c), dtype = np.uint8) * 254
#取得lena影像的高七位
lenaH7 = cv2.bitwise_and(lena, t254)
#將watermark嵌入lenaH7內
e = cv2.bitwise_or(lenaH7, watermark)
#==============分析過程=================
#產生元素值都是1的陣列
t1 = np.ones((r, c), dtype = np.uint8)
#從載體影像內分析浮水印影像
wm = cv2.bitwise_and(e, t1)
print(wm)
#將浮水印影像內的值1處理維255,以方便顯示
#後續章節會介紹使用threshold實現
w = wm[:, :] > 0
wm [w] = 255
#==============顯示=====================
cv2.imshow("lena", lena)
cv2.imshow("watermark", watermark * 255)
cv2.imshow("e", e)
cv2.imshow("wm", wm)
cv2.waitKey()
cv2.destroyAllWindows()
