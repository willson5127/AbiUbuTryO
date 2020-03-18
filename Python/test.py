# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 00:16:16 2020

@author: willson
"""

import pyautogui

pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True
width, height = pyautogui.size()
x, y = pyautogui.position()