import cv2
import numpy as np
from matplotlib import pyplot as plt
def scale(img):
	img -= np.min(img)
	img = np.multiply(255.0/np.max(img),img)
	return img.astype(dtype = np.uint8)

def Magnitude_and_Phase(img):
	f = np.fft.fft2(img)
	fshift = np.fft.fftshift(f)
	magnitude = np.abs(fshift)
	phase = np.angle(fshift)
	return (magnitude,phase)

def reconstruct(mag,phase):
	freq_img = mag*np.cos(phase) + 1j*mag*np.sin(phase)
	img = np.fft.ifftshift(freq_img)
	img = np.abs(np.fft.ifft2(img))
	return img
	#f = np.fft.fft2(new)
	#fshift = np.fft.fftshift(f)
	#fshift[new.shape[0]/2-30:new.shape[0]/2+30,new.shape[1]/2-30:new.shape[1]/2+30] = 0
	#f_ishift = np.fft.ifftshift(fshift)

mandril = cv2.imread("mandrill.tif",0)
clown = cv2.imread("clown.tif",0)
(mandril_mag,mandril_phase) = Magnitude_and_Phase(mandril)
(clown_mag,clown_phase) = Magnitude_and_Phase(clown)
cv2.imwrite("mandril_phase.png",scale(mandril_phase))
cv2.imwrite("mandril_mag.png",scale(20*np.log(mandril_mag)))
cv2.imwrite("clown_phase.png",scale(clown_phase))
cv2.imwrite("clown_mag.png",scale(20*np.log(clown_mag)))
#reconstruct(mandril_mag,mandril_phase)
#new = np.multiply(mandril_mag,mandril_phase)
cv2.imwrite("mandril_mag_clown_phase.png",scale(reconstruct(mandril_mag,clown_phase)))
cv2.imwrite("clown_mag_mandril_phase.png",scale(reconstruct(clown_mag,mandril_phase)))