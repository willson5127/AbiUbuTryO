# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import serial

s = serial.Serial("COM3", 9600)

while True:
    print(s.readline())