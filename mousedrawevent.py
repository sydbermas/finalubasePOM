import math
from PIL.ImageOps import grayscale
import cv2
import pyautogui
import numpy as np
import glob
import auto
class DrawLineWidget(object):
   
    def __init__(self):
        self.original_image = cv2.imread('SavedImages\imageCap.jpg')
        self.clone = self.original_image.copy()

        cv2.namedWindow('image')
        
        cv2.setMouseCallback('image', self.extract_coordinates)

        # List to store start/end points
        self.image_coordinates = []

    def extract_coordinates(self, event, x, y, flags, parameters):
        # Record starting (x,y) coordinates on left mouse button click
        if event == cv2.EVENT_LBUTTONDOWN:
            self.image_coordinates = [(x,y)]
            

        # Record ending (x,y) coordintes on left mouse bottom release
        elif event == cv2.EVENT_LBUTTONUP:
            self.image_coordinates.append((x,y))
            print('Starting: {}, Ending: {}'.format(self.image_coordinates[0], self.image_coordinates[1]))
            distA = math.sqrt((self.image_coordinates[1][0] -self.image_coordinates[0][0])**2 + (self.image_coordinates[1][1] -self.image_coordinates[0][1])**2)
            A = (distA/14.5)
            print("A:"+str(round(A,2))+"inches")

            # Draw line
            cv2.line(self.clone, self.image_coordinates[0], self.image_coordinates[1], (0,0,0), 2)
            cv2.imshow("image", self.clone)
             

        # Clear drawing boxes on right mouse button click
        elif event == cv2.EVENT_RBUTTONDOWN:
            self.clone = self.original_image.copy()
            
    def show_image(self):

        return self.clone

if __name__ == '__main__':
    draw_line_widget = DrawLineWidget()
        
    while True:
        cv2.imshow('image', draw_line_widget.show_image())
        
        start = cv2.waitKey(1)
        key = cv2.waitKey(1)
        
        if key == ord(' '):
            auto.bot()
        # Close program with keyboard 'q'
        if key == ord('q'):
            auto.bot()
            cv2.destroyAllWindows()
            exit(1)

