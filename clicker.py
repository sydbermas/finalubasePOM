from tkinter.constants import LEFT
import cv2
import pyautogui
import os, time
import win32gui, win32con
from PIL import Image
from PIL import ImageChops

import datetime

def imgAutoCick(tempFile, whatDo, debug=False):
    '''
        temFile :The small picture that needs to be matched
        whatDo  :Required action
                pyautogui.moveTo(w/2, h/2)# Basic movement
                pyautogui.leftClick()  # Left click
                pyautogui.dragTo()  # drag mouse to X of n, Y of n while holding down left mouse button
                pyautogui.drag(w/2, h/2)
                pyautogui._mouseMoveDrag(w/2, h/2)
                pyautogui.mouseUp()
                pyautogui.mouseDown(w/2, h/2, 1, 0, 2)
                pyautogui.doubleClick(w/2, h/2)  # Double left click
                pyautogui.click()
                pyautogui.rightClick(w/2, h/2) # Right-click
                pyautogui.middleClick() # Middle click
                pyautogui.tripleClick() # Mouse current position 3 clicks
                pyautogui.scroll(10) # Roll the wheel up by 10, pay attention to the direction, and go down for negative values
        
    More details：https://blog.csdn.net/weixin_43430036/article/details/84650938
        debug   :Whether to open the display debugging window
    '''
 
    pyautogui.screenshot('screenshot.png')

 
    gray = cv2.imread("screenshot.png",0)
    
    img_template = cv2.imread(tempFile,0)

    w, h = img_template.shape[::-1]

    res = cv2.matchTemplate(gray,img_template,cv2.TM_SQDIFF)
    
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    

    top = min_loc[0]
    left = min_loc[1]
    x = [top, left, w, h]

    top_left = min_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)

    pyautogui.moveTo(top+h/2, left+w/2)
    whatDo(x)

def measurer_bot(): # Acting list images from google sheet
    imgAutoCick("7M71906\Front\A\\a.jpg", pyautogui.doubleClick)
    imgAutoCick("7M71906\Front\A\\b.jpg", pyautogui.rightClick)
    imgAutoCick("7M71906\Front\B\\a.jpg", pyautogui.doubleClick)
    imgAutoCick("7M71906\Front\B\\b.jpg", pyautogui.rightClick)
    imgAutoCick("7M71906\Front\C\\a.jpg", pyautogui.doubleClick)
    imgAutoCick("7M71906\Front\C\\b.jpg", pyautogui.rightClick)
    imgAutoCick("7M71906\Front\D\\a.jpg", pyautogui.doubleClick)
    imgAutoCick("7M71906\Front\D\\b.jpg", pyautogui.rightClick)
if __name__=="__main__":
    measurer_bot()


