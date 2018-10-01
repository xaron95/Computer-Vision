import numpy as np
import cv2
from matplotlib import pyplot as plt
x = cv2.imread("example.jpg",0)
y = x.max()
z = np.where(x==y)
r = z[0]
c = z[1]
print "Rows: "+str(r)
print "Columns: "+str(c)