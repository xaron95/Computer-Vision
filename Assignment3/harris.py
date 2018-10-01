import cv2
import numpy as np
from scipy import ndimage
from scipy import signal

img1 = cv2.imread("grid1.jpg")
img2 = cv2.imread("grid2.jpg")
img3 = cv2.imread("grid3.jpg")
img4 = cv2.imread("grid_rotated.jpg")

def harris_response(image,k=0.04,threshold=0.1):
	gauss = np.array([[0.0625,0.125,0.0625],[0.125,0.25,0.125],[0.0625,0.125,0.0625]])
	gx = np.array([[0,0,0],[-1,0,1],[0,0,0]])
	gy = np.array([[0,-1,0],[0,0,0],[0,1,0]])
	img = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
	img = signal.convolve(img,gauss,mode='same')

	Ix = signal.convolve2d(img,gx,mode='same')
	Iy = signal.convolve2d(img,gy,mode='same')


	Ixx = signal.convolve(Ix*Ix,gauss,mode='same')
	Ixy = signal.convolve(Ix*Iy,gauss,mode='same')
	Iyy = signal.convolve(Iy*Iy,gauss,mode='same')

	det = Ixx*Iyy - Ixy**2
	trace = Ixx + Iyy

	harris_img = det - k*trace**2
	image[harris_img>threshold*harris_img.max()] = [255,0,0]
	return image

cv2.imwrite("corners_grid1.png",harris_response(img1))
cv2.imwrite("corners_grid2.png",harris_response(img2))
cv2.imwrite("corners_grid3.png",harris_response(img3))
cv2.imwrite("corners_grid_rotated.png",harris_response(img4))
