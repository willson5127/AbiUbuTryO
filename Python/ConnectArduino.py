# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

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
        
def doit(stop_event, arg):
    while not stop_event.wait(0.01):
        print(s.readline())
    print("Stopping as you wish.")

def readAD():
    while True:
        print(s.readline())  

s = serial.Serial("COM6", 9600)
t1 = threading.Thread(target = readAD)
status = True

posx = np.array([1540,230,1320,1560,290, 795,1500,990
,1630,925,925,1540,1160,1630,925,926,1540 ,120])
posy = np.array([500,720,770,890,470 ,480,670,485 ,930,600
                 ,600,950,480,930,600,601,950,100])

pill2kill = threading.Event()
t1 = threading.Thread(target=doit, args=(pill2kill, "task"))
t1.start()

try:
        
    while status:        
        select = input("Please insert command!")
        for case in switch(select):
            if case("start"):
                time.sleep(2)
                for j in range(2):
                    for i in range(len(posx)):
                        x, y = pyautogui.position()
                        xd = posx[i] - x                
                        yd = posy[i] - y                
                        s.write(b'Move*\r\n')
                        s.write(str.encode('%s\r\n' % (xd)))
                        s.write(str.encode('%s\r\n' % (yd)))
                        s.write(b'ClickLeftBTN*\r\n')
                        time.sleep(4)
                        if ((i == 11) | (i == 16)):
                            time.sleep(30)
                        nx, ny = pyautogui.position()
                        print (nx , "," , ny)
            elif case("exit"):
                status = False
            break
        
    pill2kill.set()    
    s.close()
        
except:
    pill2kill.set()
    s.close()
    