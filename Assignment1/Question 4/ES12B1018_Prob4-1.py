import numpy as np
import cv2
from matplotlib import pyplot as plt
x = cv2.imread("example.jpg",0)
y = np.sort(x,axis=None)
y = y[::-1]
plt.plot(y)
plt.show()
cv2.waitKey(0)