import math
from typing import IO
from PIL.ImageOps import grayscale
import cv2
import pyautogui
import numpy as np
import glob
import clicker
import time
class DrawLineWidget(object):
   
    def __init__(self):
        self.original_image = cv2.imread('SavedImages\imageCap.jpg')
        self.clone = self.original_image.copy()

        cv2.namedWindow('AutoMeasure')
        
        cv2.setMouseCallback('AutoMeasure', self.extract_coordinates)

        # List to store start/end points
        self.image_coordinates = []

    def extract_coordinates(self, event, x, y, flags, parameters):
        # Record starting (x,y) coordinates on left mouse button click
        if event == cv2.EVENT_LBUTTONDBLCLK:
            self.image_coordinates = [(x,y)]
            

        # Record ending (x,y) coordintes on left mouse bottom release
        elif event == cv2.EVENT_RBUTTONDOWN:
            self.image_coordinates.append((x,y))
            print('Starting: {}, Ending: {}'.format(self.image_coordinates[0], self.image_coordinates[1]))
            distA = math.sqrt((self.image_coordinates[1][0] -self.image_coordinates[0][0])**2 + (self.image_coordinates[1][1] -self.image_coordinates[0][1])**2)
            dist = (distA/14.5)
            print("POMID:"+str(round(dist,2))+"inches")

            # Draw line
            cv2.line(self.clone, self.image_coordinates[0], self.image_coordinates[1], (0,0,0), 1)
            cv2.putText(self.clone,("POMID:"+str(round(dist,2))+"inches"),(self.image_coordinates[0]),cv2.FONT_HERSHEY_SIMPLEX,0.4,(0,0,0),1)
            cv2.imshow("AutoMeasure", self.clone)
             

        # Clear drawing boxes on right mouse button click
        elif event == cv2.EVENT_LBUTTONDBLCLK:
            self.clone = self.original_image.copy()
            
    def show_image(self):
        
        return self.clone

if __name__ == '__main__':
    draw_line_widget = DrawLineWidget()
    pyautogui.typewrite("s")
    while True:
        cv2.imshow('AutoMeasure', draw_line_widget.show_image())
        cv2.moveWindow("AutoMeasure", 40,30)

        key = cv2.waitKey(1)
        start = cv2.waitKey(1)
        if key == ord('s'):
            exec(open("clicker.py").read())
        # Close program with keyboard 'q'
        if key == ord(' '):
            cv2.destroyWindow("AutoMeasure")
            break
        
        
        
            


