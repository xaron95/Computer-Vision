import cv2
import numpy as np
from scipy import ndimage
from scipy import signal

def scale(img):
	img -= np.min(img)
	img = np.multiply(255.0/np.max(img),img)
	return np.array(img,dtype = np.uint8)
def impulse(row,column):
	imp = np.zeros((row,column))
	imp[row/2][column/2] = 1
	return imp
def filter_fourier(img,filter):
	f = np.fft.fft2(img)
	fshift = np.fft.fftshift(f)
	return fshift*filter
def inverse_fft(img):
	img = np.fft.ifftshift(img)
	return np.fft.ifft2(img)
def hybrid_conv(img1,img2,cutoff_freq):
	gauss_filter = ndimage.filters.gaussian_filter(impulse(img1.shape[0],img1.shape[1]),cutoff_freq)
	gauss_filter = gauss_filter/np.max(gauss_filter)
	img1blue = filter_fourier(img1[:,:,0],gauss_filter)
	img1green = filter_fourier(img1[:,:,1],gauss_filter)
	img1red = filter_fourier(img1[:,:,2],gauss_filter)
	img2blue = filter_fourier(img2[:,:,0],(1-gauss_filter))
	img2green = filter_fourier(img2[:,:,1],(1-gauss_filter))
	img2red = filter_fourier(img2[:,:,2],(1-gauss_filter))
	hybblue = img1blue+img2blue
	hybgreen = img1green+img2green
	hybred = img1red+img2red
	b = inverse_fft(hybblue)
	g = inverse_fft(hybgreen)
	r = inverse_fft(hybred)
	hybrid_img = cv2.merge((b.real,g.real,r.real))
	return hybrid_img

img1 = cv2.imread("plane.bmp")
img2 = cv2.imread("bird.bmp")
cv2.imwrite("hyb.png",scale(hybrid_conv(img1,img2,10)))