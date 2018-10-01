import numpy as np
import cv2
from matplotlib import pyplot as plt
x = cv2.imread("example.jpg",0)
y = np.zeros((100,100,3),dtype='uint8')
#Threshold is 127
ret,y[:,:,2] = cv2.threshold(x,127,255,cv2.THRESH_BINARY)
cv2.imshow('Swapped',y)
cv2.waitKey(0)