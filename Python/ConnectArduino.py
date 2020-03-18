# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import serial
import threading
import time
import pyautogui
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

pill2kill = threading.Event()
t1 = threading.Thread(target=doit, args=(pill2kill, "task"))
t1.start()

try:
        
    while status:        
        select = input("Please insert command!")
        for case in switch(select):
            if case("start"):
                x, y = pyautogui.position()
                xd = 800 - x
                x100 = xd / 100
                x100 = math.floor(x100)
                xn = xd % 100
                yd = 600 - y
                y100 = yd / 100
                y100 = math.floor(y100)
                yn = yd % 100
                
                xe = 1
                ye = 1
                b100 = 0
                if (x100 < 0):
                    xe = -1
                xn = xe * xn
                if (y100 < 0):
                    ye = -1
                yn = ye * yn
                if (abs(x100) >= abs(y100)):
                    b100 = x100
                elif (abs(x100) < abs(y100)):
                    b100 = y100
                for i in range(abs(b100)):
                    if ((i + 1) > abs(x100)):
                        xe = 0
                    elif ((i + 1) > abs(y100)):
                        ye = 0
                    s.write(b'Move*\r\n')
                    s.write(str.encode('%s\r\n' % (xe * 10)))
                    s.write(str.encode('%s\r\n' % (ye * 10)))
                s.write(b'Move*\r\n')
                s.write(str.encode('%s\r\n' % xn))
                s.write(str.encode('%s\r\n' % yn))
                    
                
                
                
                
                s.write(b'ClickRightBTN*\r\n')
            elif case("exit"):
                status = False
            break
        
    pill2kill.set()    
    s.close()
        
except:
    pill2kill.set()
    s.close()
    