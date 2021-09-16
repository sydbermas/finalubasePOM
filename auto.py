from tkinter.constants import LEFT
import cv2
import pyautogui
import os, time
import win32gui, win32con

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
                pyautogui.doubleClick(w/2, h/2,)  # Double left click
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

    # if debug:

    #     img = cv2.imread("screenshot.png",1)

    #     cv2.rectangle(img,top_left, bottom_right, (0,0,255), 2)

    #     img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5, interpolation=cv2.INTER_NEAREST)
    #     cv2.imshow("processed",img)
    #     cv2.waitKey(0)

    #     cv2.destroyAllWindows()
    # os.remove("screenshot.png")

# def simple_example_baidu():
  
#     # time.sleep(2)
#     # imgAutoCick("7W82995\A\\b.jpg", pyautogui.dragTo)

#     # time.sleep(2)
#     # imgAutoCick("7W82995\A\\b.jpg", pyautogui.mouseUp)

#     # time.sleep(1)
#     # pyautogui.typewrite("meinv1")

#     # time.sleep(1)
#     # imgAutoCick("baidu_tu/test4.png", pyautogui.click)
 
#     # time.sleep(1)
#     # imgAutoCick("baidu_tu/test5.png", pyautogui.click)

#     m, n = pyautogui.size()
#     pyautogui.moveTo(x=m/2, y=n/2)

#     for i in range(100):
#         time.sleep(0.5)
#         pyautogui.scroll(-120) 

if __name__=="__main__":
  
    # Minimize = win32gui.GetForegroundWindow()
    # win32gui.ShowWindow(Minimize, win32con.SW_MINIMIZE)

    # pyautogui.PAUSE = 1
    # pyautogui.press('winleft')
    # pyautogui.PAUSE = 1

    imgAutoCick("7W82995\A\\a.jpg", pyautogui.doubleClick)
    imgAutoCick("7W82995\A\\b.jpg", pyautogui.rightClick)
    
    
    
