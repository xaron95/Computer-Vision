import numpy as np
import cv2
from matplotlib import pyplot as plt
x = np.array([1,2,3,4,5,6],dtype='uint8').T
y = np.reshape(x,(2,3),order='F')
print y