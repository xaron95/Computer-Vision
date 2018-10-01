import numpy as np
import cv2
from matplotlib import pyplot as plt
x = cv2.imread("example.jpg",0)
y = x[50:100,:50]
cv2.imshow("quadrant",y)
cv2.waitKey(0)