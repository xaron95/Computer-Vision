import cv2
import numpy as np 
from matplotlib import pyplot as plt 

def sobel(img):
	x = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=3)
	y = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=3)
	return x,y

def orientation(x,y):
	return np.arctan2(x,y)

def scale(mag,angle,t=0):
	direction = np.round(np.divide(angle,np.pi/4))
	direction[mag<t*mag.max()] = 8
	return direction
