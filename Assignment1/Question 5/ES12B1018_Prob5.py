import numpy as np
import cv2
from matplotlib import pyplot as plt

import ES12B1018_Prob5_1 as func1
import ES12B1018_Prob5_2 as func2
import ES12B1018_Prob5_3 as func3
import ES12B1018_Prob5_4 as func4
import ES12B1018_Prob5_5 as func5

grayimg = cv2.imread("einstein.jpg",0)
colorimg = cv2.imread("example2.jpg")
colorcopyimg = cv2.cvtColor(colorimg,cv2.COLOR_BGR2RGB)

negimg = func1.negative_img(grayimg)
mirrorimg = func2.mirror_img(grayimg)
avgimg = func4.avg_mirror(grayimg)
rngimg = func5.random_img(grayimg)
swapimg = func3.redgreen_swap(colorimg)
swapimg = cv2.cvtColor(swapimg,cv2.COLOR_BGR2RGB)

plt.subplot(251)
plt.imshow(grayimg,'gray')
plt.title("Original grayscale image")
plt.xticks([])
plt.yticks([])
plt.subplot(252)
plt.imshow(negimg,'gray')
plt.title("Negative image")
plt.xticks([])
plt.yticks([])
plt.subplot(253)
plt.imshow(mirrorimg,'gray')
plt.title("Mirror image")
plt.xticks([])
plt.yticks([])
plt.subplot(254)
plt.imshow(avgimg,'gray')
plt.title("Averaged image")
plt.xticks([])
plt.yticks([])
plt.subplot(255)
plt.imshow(rngimg,'gray')
plt.title("Random subtracted image")
plt.xticks([])
plt.yticks([])
plt.subplot(256)
plt.imshow(colorcopyimg)
plt.title("Original coloured image")
plt.xticks([])
plt.yticks([])
plt.subplot(257)
plt.imshow(swapimg)
plt.title("Swapped coloured image")
plt.xticks([])
plt.yticks([])
plt.show()