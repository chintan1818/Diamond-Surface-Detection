import time

import pyautogui


im1 = pyautogui.screenshot(region=(500,200,600,400))
im1.save("savedimage.png")