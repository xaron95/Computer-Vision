import numpy as np
import cv2
from matplotlib import pyplot as plt
x = cv2.imread("example.jpg",0)
plt.hist(x.ravel(),20,[0,256])
plt.show()
cv2.waitKey(0)