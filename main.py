from pyautogui import *
import pyautogui
import time
import keyboard
import numpy as np
import random
import win32api, win32con
import PIL
import cv2



def findImageAndClick(location):

    while 1:
        r = pyautogui.locateOnScreen(location, grayscale=True, confidence=0.9)
        if r is not None:
            click((
                (r.left+r.left+r.width)/2
            ),(
                 (r.top + r.top + r.height) / 2
            ))
            print(r)
            break
        else:
            print("waiting for image")
def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

findImageAndClick("chrome.png")




# time.sleep(2)
# pyautogui.keyDown('1');
# pyautogui.press('1',10);
# click(45,1040)
# click(45,1040)
# click(45,1040)
# click(45,1040)
# click(45,1040)
# click(45,1040)

# if pyautogui.pixel(300,500) == (60,63,65):
#         print("yes")
# else:
#         print("no")


# while keyboard.is_pressed('q')== False:
#     print("not yet")


