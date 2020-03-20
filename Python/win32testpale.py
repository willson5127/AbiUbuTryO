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
    
    frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2GRAY)
    cv2.imshow("svreen box", frame)
    k = cv2.waitKey(30)&0xFF
    
    if k == 27:
        cv2.destroyAllWindows()
        break
    



