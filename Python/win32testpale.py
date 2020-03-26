# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 17:25:13 2020

@author: willson
"""

from PIL import ImageGrab
import numpy as np

import threading

import cv2
import win32gui

'''
def Opencv(stop_event, arg):
    while not stop_event.wait(0.01):
        
t1 = threading.Thread(target = Opencv)
       ''' 


handle = win32gui.FindWindow(None, "BlueStacks") 
print("代碼:", handle)

while True:
    try:
        left, top, right, bottom = win32gui.GetWindowRect(handle)
        print("左:", left, "上:", top, "右:", right, "下:", bottom)
        
        hwndDC = win32gui.GetWindowDC(handle)
        
        title = win32gui.GetWindowText(handle)
        print ("標題:", title)
        clsname = win32gui.GetClassName(handle)   
        print ("類名:", clsname)
        
        print(handle)
        
        print("%x" %handle)
        
    except:
        print ("找不到視窗")
        break
    
    img = ImageGrab.grab(bbox = (left, top, right, bottom))
    img_np = np.array(img)
    
    tem001 = cv2.imread("Template/test/WeighAnchor.PNG", 1)
    cv2.imshow("tem", tem001)
    
    frame0 = cv2.cvtColor(img_np, cv2.COLOR_BGR2HSV)
    miny = np.array([80, 50, 50])
    maxy = np.array([110, 255, 255])
    mask = cv2.inRange(frame0, miny, maxy)
    
    #t1, thd = cv2.threshold(frame0, 127, 255, cv2.THRESH_BINARY)
    #t2, otsu = cv2.threshold(frame0, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    #cv2.imshow("img", img)
    #cv2.imshow("thd", thd)
    #cv2.imshow("otsu", otsu)
    
    frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
    cv2.imshow("MAIN", frame)
    
    y = cv2.bitwise_and(frame, frame, mask = mask)
    cv2.imshow('yello', y)
    
    try:
        Scan = cv2.matchTemplate(frame, tem001, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(Scan)
        cv2.imshow("SCAN", Scan)
        print(min_val, max_val, min_loc, max_loc)
        #corner_loc = (max_loc[0] + 50, max_loc[1] + 150)
        #cv2.rectangle(frame, max_loc, min_loc, (0, 0, 255), 5)
        
        corner_loc = (max_loc[0] + 200, max_loc[1] + 200)
        player_spot = (max_loc[0] + 25, max_loc[1] + 150)
        cv2.circle(frame, player_spot, 10, (0, 255, 255), -1)
        cv2.rectangle(frame, max_loc, corner_loc, (0, 0, 255), 5)
    except:
        print("無法抓取影像") 
        
    cv2.imshow("MAIN", frame)
    
    
        
    k = cv2.waitKey(30)&0xFF
    
    if k == 27:
        cv2.destroyAllWindows()
        break
    



