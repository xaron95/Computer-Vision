import numpy as np
import cv2
from matplotlib import pyplot as plt
x = cv2.imread("example.jpg",0)
y = cv2.mean(x.flatten())
x = cv2.subtract(x,y)
cv2.imshow("image",x)
cv2.waitKey(0)