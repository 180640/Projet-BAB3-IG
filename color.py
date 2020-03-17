# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 09:52:00 2020

@author: Céliane
"""

import cv2 as cv
from matplotlib.pyplot import *
import numpy
import math
            

img1 = cv.imread("fig_color_3.png")
img2 = cv.cvtColor(img1,cv.COLOR_BGR2RGB)
figure(figsize=(4,4))
imshow(img2)
            

red,green,blue = cv.split(img2)
figure(figsize=(12,4))             

hsv = cv.cvtColor(img1,cv.COLOR_BGR2HSV)
hue,sat,val = cv.split(hsv)
figure(figsize=(12,4))         
              

lower = numpy.array([90/2,100,50],dtype=numpy.uint8)
upper = numpy.array([120/2,255,255],dtype=numpy.uint8)
seg = cv.inRange(hsv,lower,upper)
figure(figsize=(4,4))
imshow(seg,cmap=cm.gray)