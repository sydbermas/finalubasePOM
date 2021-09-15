import pyautogui
import glob
import cv2


def bot():
    pyautogui.screenshot('screenshot.jpg')  
    imageToBeInspected = 'screenshot.jpg'  
    poms = [glob.glob('7W82995\B\\*.jpg')]

    for pom in poms:

        img = cv2.imread(imageToBeInspected,0)
        img2 = img.copy()
        
        templAB = cv2.imread(pom[0],0) # pom start
        templBA = cv2.imread(pom[1],0)
        w, h = templAB.shape[::-1]
        w2, h2 = templBA.shape[::-1]
        # All the 6 methods for comparison in a list
        methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
                'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']
        meth = methods[1] # Mehtod setting
        img = img2.copy()
        methodAB = eval(meth)
        # Apply template Matching
        res = cv2.matchTemplate(img,templAB,methodAB)
        res2 = cv2.matchTemplate(img,templBA,methodAB)
        
        _, _, min_loc, max_loc = cv2.minMaxLoc(res)
        _, _, min_loc2, max_loc2 = cv2.minMaxLoc(res2)
        
        # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
        if methodAB in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
            top_left = min_loc
            top_left2 = min_loc2

        else:
            Btl = max_loc
            Btl2 = max_loc2

    pyautogui.move(Btl[0],Btl[1],0.5)