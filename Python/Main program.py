# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 22:07:13 2020

@author: willson

Main program test version
"""
from PIL import ImageGrab
import numpy as np
import cv2
import win32gui

import serial
import threading
import time
import pyautogui
import numpy as np
import math

class switch(object):
    def __init__(self, value):
        self.value = value
        self.fall = False
    def __iter__(self):
        """Return the match method once, then stop"""
        yield self.match
        raise StopIteration
    def match(self, *args):
        """Indicate whether or not to enter a case suite"""
        if self.fall or not args:
            return True
        elif self.value in args: # changed for v1.5, see below
            self.fall = True
            return True
        else:
            return False
        
player_spot = (0, 0)
min_val, max_val, min_loc, max_loc = 0, 0, (0, 0), (0, 0)
'''Opencv Template function'''
def TemplateSacn(src, tem):
    Scan = cv2.matchTemplate(src, tem, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(Scan)
    #print(max_loc, "\n")
    player_spot = (max_loc[0] + 50, max_loc[1] + 50)
    '''test for show'''
    cv2.rectangle(src, max_loc, (max_loc[0] + 50, max_loc[1] + 50), (0, 0, 255), 5)
    return min_val, max_val, min_loc, max_loc, player_spot

'''ArduinoMICRO Mouse action function'''
def MouseAct(Tarx, Tary, Wleft, Wtop):
    x, y = pyautogui.position()
    xd = Wleft + Tarx - x                
    yd = Wtop + Tary - y
    s.write(b'Move*\r\n')
    s.write(str.encode('%s\r\n' % (xd)))
    s.write(str.encode('%s\r\n' % (yd)))
    s.write(b'ClickLeftBTN*\r\n')    
        
pill2kill = threading.Event()
def readAD(stop_event, arg):
    while not stop_event.wait(0.1):
        print(s.readline())
    print("Stopping as you wish.")


    
pill2kill2 = threading.Event()
def process(stop_event, arg):
    
    station1_1_Page = [-1, 1, 2, 3, 4, 5, 4, 5, 1]
    station1_1_Act = [1, 3, 4, 5, 6, 7, 8, 7, 2]
    PageStatus = station1_1_Page
    ActStatus = station1_1_Act
    ii = 0     
    
    while not stop_event.wait(3):    
                
        max_loc_range = (155, 120, 135, 52)
        
        try:
            handle = win32gui.FindWindow(None, "BlueStacks")
            left, top, right, bottom = win32gui.GetWindowRect(handle)
        except:
            print ("找不到視窗\n")
            break
        img = ImageGrab.grab(bbox = (left, top, right, bottom))
        img_np = np.array(img)
        frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
        cv2.imshow("MAIN", frame)
        
        pagest = ""
        pagename = ""
        if PageStatus[ii] == 1:
            pagest = "Template/test/PageName/WarPage(Strike).PNG"
            pagename = "War Map"
        elif PageStatus[ii] == 2:
            pagest = "Template/test/MiniWindowName/Stage1-1(Mini).PNG"
            pagename = "1-1 Mini Page"
            max_loc_range = (470, 340, 240, 215)
            
        elif PageStatus[ii] == 3:
            pagest = "Template/test/MiniWindowName/FleetSelect(Mini).PNG"
            pagename = "Fleet Select Mini Page"
            max_loc_range = (270, 130, 155, 115)
            
        elif PageStatus[ii] == 4:
            pagest = "Template/test/PageName/SubChapter(INWarMap).PNG"
            pagename = "IN WAR Map"
            time.sleep(2)
        elif PageStatus[ii] == 5:
            pagest = "Template/test/PageName/Formation(FormationPage).PNG"
            pagename = "Formation Page"
        elif PageStatus[ii] == 6:
            pagest = "Template/test/PageName/Auto(INWARPage).PNG"
            pagename = "IN WAR Page"
        else:
            pagest = "Template/test/PageName/UserName.PNG"
            pagename = "Main Page"
        
        try:
            tem001 = cv2.imread(pagest, 1)
            min_val, max_val, min_loc, max_loc, player_spot = TemplateSacn(frame, tem001)
            cv2.imshow("MAIN", frame)
            print("目前狀態 : ", pagename) 
        except:
            print("取樣失敗!\n")
        
        print(max_loc)
                  
        if (max_loc_range[0] > max_loc[0] > max_loc_range[1]) and (max_loc_range[2] > max_loc[1] > max_loc_range[3]):
            
            btnst = ""
            if ActStatus[ii] == 1:
                btnst = "Template/test/Button/WeighAnchor.PNG"
            elif ActStatus[ii] == 2:
                btnst = "Template/test/Button/WarPage(Back).PNG"
            elif ActStatus[ii] == 3:
                btnst = "Template/test/Button/Stage1-1(WarPage).PNG"
            elif ActStatus[ii] == 4:
                btnst = "Template/test/MiniWindowButton/ImmediateStart(Mini).PNG"
            elif ActStatus[ii] == 5:
                btnst = "Template/test/MiniWindowButton/Formation(Mini).PNG"
            elif ActStatus[ii] == 6:
                btnst = "Template/test/Emeny/Destroyer(Emeny).PNG"
            elif ActStatus[ii] == 7:
                btnst = "Template/test/Button/WeighAnchor(FormationPage).PNG"
            elif ActStatus[ii] == 8:
                btnst = "Template/test/Emeny/Boss(Emeny).PNG"
                
            try:
                tem001 = cv2.imread(btnst, 1)
                min_val, max_val, min_loc, max_loc, player_spot = TemplateSacn(frame, tem001)
                cv2.imshow("MAIN", frame)
                print("執行動作")
                MouseAct(max_loc[0] + 50, max_loc[1] + 50, left, top)
                ii += 1
            except:
                print("取樣失敗!\n")


        '''btnst = ""
        for i in range(4):
            if i == 0:
                btnst = "Template/test/Button/AutoWar(OFF).PNG"
            elif i == 1:
                btnst = "Template/test/Button/TouchToContinue.PNG"
            elif i == 2:
                btnst = "Template/test/Button/TouchToContinue2.PNG"
            elif i == 3:
                btnst = "Template/test/Button/confirm.PNG"
            
            try:
                tem001 = cv2.imread(btnst, 1)
                min_val, max_val, min_loc, max_loc, player_spot = TemplateSacn(frame, tem001)
                cv2.imshow("MAIN", frame)
                print("執行動作")
                time.sleep(0.5)
                MouseAct(max_loc[0] + 10, max_loc[1] + 10, left, top)
            except:
                print("取樣失敗!\n")'''

        
        k = cv2.waitKey(30)&0xFF
        if k == 27:
            cv2.destroyAllWindows()
            break
        
    print("Stopping as you wish2.")

s = serial.Serial("COM6", 9600)
t1 = threading.Thread(target = readAD, args=(pill2kill, "task"))
status = True
t1.start()

try:
        
    while status:        
        select = input("Please insert command!")
        for case in switch(select):
            if case("start"):
                pill2kill2.clear()
                t2 = threading.Thread(target = process, args=(pill2kill2, "task"))
                t2.start()
            elif case("stop"):
                pill2kill2.set()
            elif case("exit"):
                status = False
            break
        
    pill2kill.set()
    pill2kill2.set()
    s.close()
        
except:
    pill2kill.set()
    pill2kill2.set()
    s.close()