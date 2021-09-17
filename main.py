import math
import tkinter
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
import glob
import imutils
import time
from fractions import Fraction
from tkinter import *
from numpy.core.fromnumeric import amax, shape
from numpy.lib.function_base import delete, median
from math import dist

from scipy.spatial import distance
from collections import namedtuple
from itertools import product
import utility
import sys
import cv2
import imutils

images,names = utility.readImages()
descriptors = utility.getDescriptors(images)
# cap=cv2.VideoCapture("test.mp4")	#using video
cap=cv2.VideoCapture(0,cv2.CAP_DSHOW)				#Runtime camera
while(cap.isOpened()):
	success,frame=cap.read()
	if success:
		frame=imutils.resize(frame,width=640)
		gray_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
		name = utility.findMatch(gray_frame,descriptors,names)
		cv2.putText(frame,name,(20,20),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,0,0),2)
		
		cv2.imshow("Ubase APM",frame)

		start = cv2.waitKey(1)
		key = cv2.waitKey(1)

		if start==ord(' '):
			root = Tk()
			root.withdraw()
			
			if name == "":
				
				tkinter.messagebox.showinfo(title='Image Error', message='Style and Levels are not accepted.')
				print('Style and Levels are not accepted.')
				
			elif '-' in name:
				image = 'SavedImages\\imageCap1.jpg'
				cv.imwrite(image, frame)
				

			elif '' in name:
				image = 'SavedImages\\imageCap.jpg'
			
					
				
				
		elif key==ord('q'):
			cv2.destroyAllWindows(frame)
			exit(1)
	else:
		break

cap.release()
